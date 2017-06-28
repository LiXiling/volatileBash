def rot_enc(text, offset, ignoreSpace=True, ignorePunc=False, charRange=94):
    ignoredChars = []

    result = ""

    if ignoreSpace:
        ignoredChars.extend([" ", "\t", "\n", "\r"])
    if ignorePunc:
        ignoredChars.extend([".", ",", "?", "!", ";", ":"])

    for char in text:
        if not char in ignoredChars:
            result += chr((ord(char) - 32 + offset) % charRange + 32)
        else:
            result += char

    return result