def remove_extension(s):  # return f without extension
    i = s.rfind('.')
    if(i == -1):
        return s
    else:
        return s[:i]
