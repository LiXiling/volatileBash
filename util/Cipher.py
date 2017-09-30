# -*- coding: utf-8 -*-

def rot(text, offset, ignoreSpace=True, ignorePunc=False, charRange=94):
    ignoredChars = []

    result = ""

    if ignoreSpace:
        ignoredChars.extend([" ", "\t", "\n", "\r"])
    if ignorePunc:
        ignoredChars.extend([".", ",", "?", "!", ";", ":"])

    for char in text:
        if not char in ignoredChars:
            result += chr((ord(char) - 33 + offset) % charRange + 33)
        else:
            result += char

    return result