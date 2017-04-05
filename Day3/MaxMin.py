def find_max_min(n):
    '''input -> list[]
       output -> list[]
       gives a list containing the smallest and largest number
    '''
    solution = []

    num = sorted(n)

    if num[0] == num[len(num) - 1]:
        solution.append(len(num))
        return solution

    solution.append(num[0])
    solution.append(num[len(num) - 1])

    return solution

#print(find_max_min([4, 4, 4, 4]))
   