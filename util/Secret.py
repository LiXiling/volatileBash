# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:29:02 2017

@author: Victor
"""
import string
import random        
import os
import subprocess
from util.txt2img import txt2img

class Secret():

    # Passwords that are so bad, at least the NTLM-Hash can be cracked easily.
    # Verified for all passwords via https://crackstation.net/.
    PASSWORDS =  ["123456","porsche","firebird","rosebud","password","12345678","chelsea","amateur","7777777","diamond","steelers","tiffany","jackson","scorpio","cameron","testing","mountain","shannon","madison","mustang","computer","bond007","letmein","baseball","xxxxxxxx","michael","gateway","football","phoenix","thx1138","raiders","forever","peaches","jasmine","melissa","qwertyui","jennifer","danielle","sunshine","gregory","starwars","whatever","cowboys","nicholas","swimming","trustno1","dolphin","charles","midnight","college","bulldog","1234567","ncc1701","princess","startrek","mercedes","gandalf","leather","hunting","charlie","superman","rainbow","jessica","johnson","brandon","anthony","william","ferrari","bigdaddy","chicken","heather","maverick","chicago","voyager","yankees","rangers","packers","einstein","newyork","trouble","dolphins","hardcore","redwings","winston","thunder","welcome","warrior","cocacola","panther","popular","broncos","richard","8675309","private","fornicator","zxcvbnm","blondes","michelle","victoria","corvette","fishing","matthew","patrick","marlboro","freedom","srinivas","freaking","internet","extreme","captain","redskins","abgrtyu","chester","monster","maxwell","arsenal","11111111","access14","rush2112","crystal","scorpion","iloveyou","rebecca","samantha","florida","mistress","phantom","scooter","success","albert"]
    
    def __init__(self, string=None, password=False):
        if password:
            self.secret = random.choice(self.PASSWORDS)
        else:
            self.secret = 'FLG:(' + (string if string else self._generate()) + ')'

    def _generate(self):
        # random uppercase alphanumeric string of length 6
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        
    def obfuscate(self):
        # Insert invisible Ascii control character 0x1f (Unit Separator) to
        # protect against strings and similar commands.
        # Turned out to be a bad idea - \xlf is not so invisible after all..        
        return '\x1f'.join(self.secret)
    
    def asImage(self):
        return txt2img(self.secret).img_data()
    
    def saveImage(self, path, filename = 'out.png'):
        return txt2img(self.secret).save(pathCat(path, filename))
        
    def saveZip(self, path, filename = 'out.zip', password = '', deletePng = False):
        # Only for systems where zip or 7z is installed. The python module zipfile does 
        # not support encryption, which is the only reason to zip the secret to 
        # begin with.        
        pngName = '{}.png'.format(filename.split('.')[0])
        pngPath = pathCat(path, pngName)
        filepath = pathCat(path, filename)
        # deletePng = not os.path.isfile(pngPath) 
        #if deletePng:
        self.saveImage(path, pngName)   
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

def pathCat(head, tail):
    return '{}/{}'.format(head, tail)