def max_min(n):
    '''input -> list[]
       output -> list[]
       gives a list containing the smallest and largest number
    '''
    solution = []

    num = sorted(n)
    solution.append(num[0])
    solution.append(len(num) - 1)

    return solution