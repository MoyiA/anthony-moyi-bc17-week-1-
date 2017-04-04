def data_type(n):
    
    if type(n) == type("string"):
        return len(n)
    
    if type(n) == type(None):
        return "no value"
    
    if type(n) == type(True):
        return n
    
    if type(n) == type(4):
        if n < 100:
            return "less than 100"
        if n > 100:
            return "more than 100"
        else:
            return "equal to 100"

    if type(n) == type([]):
        if len(n) < 3:
            return None
        return n[2]
    