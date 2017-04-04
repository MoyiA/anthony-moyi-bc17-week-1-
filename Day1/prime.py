def prime(n):
    '''input -> int
       output -> int
    '''
    if n == 1 or n <= 0:
        return False
    if n == 2:
        return True

    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

def prime_number(n = 1):
    '''input -> int(n)
       output -> list(prime numbers)
    '''

    if type(n) != type(6):
        return "invalid data"

    solution = []
    for i in range(0, n + 1):
        if prime(i):
            solution.append(i)
    
    return solution