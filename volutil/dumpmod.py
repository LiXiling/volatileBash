# -*- coding: utf-8 -*-
__author__ = "Victor Schümmer"
__email__ = "victor_ferdinand.schuemmer@stud.tu-darmstadt.de"

from enum import Enum
from time import time
from string import ascii_uppercase, digits
from random import choices

class State(Enum):
    READ = 0
    SIGNAL = 1
    KEYWORD = 2
    FILLER = 3
    
class Secret(Enum):
    MAILADRESS = 0
    PASSWORD = 1
    
def dumpmod(filename, count=1):
    t = time()
    buffer = []
    keywords = []
    parse(filename, buffer, keywords)
    buffer = ''.join(buffer)
    for i in range(count):
        write_file('out_' + str(i) + '.txt', apply_secrets(buffer, keywords))
    print(time() - t)
        
def parse(filename, buffer, keywords):
    keyword = ''
    state = State.READ
    with open(filename, encoding="utf8") as infile:
        for chunk in read(infile, 8192):
            for c in chunk:
                if state == State.READ:
                    if c == '!': 
                        bang = 1
                        state = State.SIGNAL
                    else:
                        write_buffer(buffer, c)
                elif state == State.SIGNAL:
                    if c == '!':
                        bang += 1
                    elif bang > 2: 
                        keyword = keyword + c
                        state = State.KEYWORD
                    else:
                        write_buffer(buffer, (bang+1) * '!')
                        state = State.READ
                elif state == State.KEYWORD:
                    if c == 'X' or c == '!':
                        keywords.append(keyword)
                        write_buffer(buffer, "%s")
                        keyword = ''
                    if c == 'X':
                        state = State.FILLER
                    elif c == '!':
                        state = State.READ
                    else:
                        keyword = keyword + c
                elif state == State.FILLER:
                    if c == '!':
                        state = State.READ
    
def write_buffer(buffer, content):
    buffer.append(content)
    #if len(buffer) > 8 * 1024 * 1024 * 10:
    #   write_file

def apply_secrets(content, keywords):
    secrets = map(lambda keyword: next_secret(keyword), keywords)
    return content % tuple(secrets)
                

def read(file, chunksize=1024):
    while True:
        data = file.read(chunksize)
        if not data:
            break
        yield data

def write_file(filename, content):
    with open(filename, 'a', encoding="utf8") as outfile:
        outfile.write(content)
        
def next_secret(keyword):
    try:
        secret_type = Secret[keyword]
    except:
        print('KeyError')
        return
    if secret_type == Secret.MAILADRESS:
        return random_string() + '@mailbox.org'
    if secret_type == Secret.PASSWORD:
        return random_string()
    
def random_string():
    return ''.join(choices(ascii_uppercase + digits, k=5))