# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:29:02 2017

@author: Victor
"""
import string
import random

class Secret():
    
    def __init__(self, string=None):
        self.secret = 'FLG:(' + (string if string else self._generate()) + ')'
        
    def _generate(self):
        #return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        
    def obfuscate(self):
        """
        Insert invisible Ascii control character 0x1f (Unit Separator) to
        protect against strings and similar commands.
        Tested with:
            Registry
            Window Title
        """
        return '\x1f'.join(self.secret)
    
    def asImage(self):
        from volutil.txt2img import txt2img
        return txt2img(self.secret).img_data()
    
    def saveImage(self, filename = 'out.png'):
        from volutil.txt2img import txt2img
        return txt2img(self.secret).save(filename)
        
    def saveZip(self, path, filename = 'out.zip', password = ''):
        """
        Only for systems where zip or 7z is installed. The python module zipfile does 
        not support encryption, which is the only reason to zip the secret to 
        begin with
        """
        import os
        import subprocess
        pngPath = '{}/{}.png'.format(path, filename.split('.')[0])
        filepath = '{}/{}'.format(path, filename)
        deletePng = not os.path.isfile(pngPath) 
        if deletePng:
            self.saveImage(pngPath)   
        try:
            subprocess.call(['zip', '--password', password, filepath, pngPath])
        except:
            try:
                subprocess.call(['7z', 'a', filepath, pngPath, '-p'+password], shell=True)
            except:
                print('Error: zip or 7z not found')
        if deletePng:
            os.remove(pngPath)
            
    
    def __str__(self):
        return self.secret