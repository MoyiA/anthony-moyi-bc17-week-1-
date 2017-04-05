def words(n):
    '''input -> "string"
       output -> dict
       counts the occurrence of character in a sentence
    '''
    solution = {}

    split_string = n.split()
    for word in split_string:
        if word in solution:
            continue
        else:
            try:
                y = int(word)
                solution[y] = 0
            except Exception:
                y = word
                solution[word] = 0

            for x in split_string:
                if x == word:
                    solution[y] += 1

    return solution
