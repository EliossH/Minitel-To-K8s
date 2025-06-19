def format_string(string, size, fill=False):
    if len(string) > size:
        return string[:size-3]+"..."
    elif fill:
        return string.ljust(size)
    return string