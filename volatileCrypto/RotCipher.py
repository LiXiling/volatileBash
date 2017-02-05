def encipher(text, offset, ignoreSpace=True, ignorePunc=False):
    ignoredChars = []

    result = ""

    if ignoreSpace:
        ignoredChars.extend([" ", "\t", "\n", "\r"])
    if ignorePunc:
        ignoredChars.extend([".", ",", "?", "!", ";", ":"])

    for char in text:
        if not char in ignoredChars:
            result += chr(ord(char) + offset)
        else:
            result += char

    return result