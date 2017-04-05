def find_missing(list_one, list_two):
    '''input -> list and list
       output -> int
    '''
    if list_one == list_two:
        return 0
    if len(list_two) > len(list_one):
        temp = list_one
        list_one = list_two
        list_two = temp

    for num in list_one:
        found = False
        for digit in list_two:
            if digit == num:
                found = True
                break
        if found  == False:
          return num

#print(find_number([4, 66, 7], [66, 77, 7, 4]))