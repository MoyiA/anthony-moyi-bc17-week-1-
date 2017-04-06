class BinarySearch(list):
    def __init__(self, length, step):
        '''input-> length: size of list
                   step of the list
        ''' 
        self.length = length
        self.step = step
        self.extend(range(step, (length * step) + 1, step))

    def search(self, value):
        '''input-> value: number being searched
           output-> dict with two keys
                    count: number of iterations for getting value
                    index: position of value in the list
        '''                    
        solution = {}
        solution["count"] = 0
        solution["index"] = -1

        start = 0
        end = self.length - 1 

        while (True):
            midpoint = (end + start) // 2

            print("start " + str(start))
            print("end " + str(end))
            print(midpoint)

            x = self[midpoint]
            if x == value:
                solution["index"] = self.index(x)
                break
            if x > value:
                end = midpoint - 1
            if x < value:
                start = midpoint + 1
            if start > end:
                break
            solution["count"] += 1
            #print("running")
            

        return solution
