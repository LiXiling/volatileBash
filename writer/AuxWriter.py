# -*- coding: utf-8 -*-

from writer.Writable import Writable

class RegistryWriter(Writable):
    
    def __init__(self):
        Writable.__init__(self)
        self.lines = []
        
    def createRegistryEntry(self, key, value, path='HKEY_CURRENT_USER\Software\MaliciousApp', 
                            valuetype="REG_SZ"):
        self.lines.append('RegWrite("{}", "{}", "{}", "{}")'.format(path, key, valuetype, value))
        self.addSolutionLine('Registry created entry with key: {}, value: {} at: {}'.format(key, value, path))
        return self
    
    def toString(self):
        return "\n".join(self.lines)

    
class AutoLogin(RegistryWriter):
   
    def enable(self, name, password, domain="", easy=False): 
        self.addSolutionLine('Windows Autologon enabled with password: "{}" (see following lines). '\
                             'Volatility commands to detect this include hivelist, printkey and lsadump. '\
                             .format(password))
        regPath = 'HKLM64\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
        self.createRegistryEntry("DefaultUserName", name, regPath)
        self.createRegistryEntry("DefaultPassword", password, regPath)
        self.createRegistryEntry("DefaultDomainName", domain, regPath)
        self.createRegistryEntry("AutoAdminLogon", "1", regPath)
        
        if (easy):
            # Secret in HKLM may actually be too hard to find. 
            # (Should be in LSADump, but we could not get it from there..)
            # Add it again to HKCU where its way easier to find. (volatility printkey)
            # Maybe the User was a bit sloppy when enabling AutoLogin ;-) 
            regPath = 'HKCU64\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
            self.createRegistryEntry("DefaultUserName", name, regPath)
            self.createRegistryEntry("DefaultPassword", password, regPath)
            self.createRegistryEntry("DefaultDomainName", domain, regPath)
            self.createRegistryEntry("AutoAdminLogon", "1", regPath)
            
        return self
    
    
class PasswordWriter(Writable):
    
    def __init__(self):
        Writable.__init__(self)
        self.password = ""
        
    def setPassword(self, password):
        self.password = password
        self.addSolutionLine('The user password of the active user (probably Eve) '\
                             'is set to "{}". The password hash can be obtained by volatility '\
                             'with "hashdump". The possible passwords are from a '\
                             'list of bad passwords and have been tested to be breakable '\
                             'with tools like crackstation.net.'\
                             .format(password))
        return self
    
    def toString(self):
        return '#RequireAdmin\n' \
            '$objUser = ObjGet("WinNT://" & @ComputerName & "/" & @UserName)\n' \
            '$objUser.SetPassword("{}")\n' \
            '$objUser.SetInfo\n'.format(self.password)
    
    
class ClipboardWriter(Writable):
    
    def __init__(self):
        Writable.__init__(self)
        self.value = ''
        
    def put(self, value):
        self.value = value
        self.addSolutionLine('The clipboard contains "{}", '\
                             'which can be obtained by volatility with "clipboard"'\
                             .format(str(self.value)))
        return self
        
    def toString(self):
        return 'ClipPut("' + str(self.value) + '")'
    