def fizzBuzz(n):
    '''input -> int
       output -> "string" or int
    '''
    
    if type(n) != type(5):
        return "Invalid Argument"
    if n <= 0:
        return n
  
    if n % 3 == 0 and n % 5 == 0:
        return "fizzBuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"

    return n