def replicate_recur(times, data):
    '''input: int(times), string or int(data)
       output: list
    '''

    solution = []

     # base case
    if times == 0 or times < 0 or type(times) == type(1/3):
        return solution

    # recurssive case    
    solution.append(data)
    times = times - 1
    others = replicate_recur(times, data)

    solution.extend(others)

    return solution
print(replicate_recur(2/5, "Hello Tony"))