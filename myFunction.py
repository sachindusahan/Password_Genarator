def strSize(arg):
    if len(arg) >= 8:
        return True
    else:
        return False

def checkDigit(arg):
    for i in arg:
        if i.isdigit():
            return True
            break
        else:
            continue
    return False

def checkUpper(arg):
    for i in arg:
        if i.isupper():
            return True
            break
        else:
            continue
    return False
