from PriorityQueue_Interface import PriorityQueue_Interface

class TwoDSequencePQ(PriorityQueue_Interface):
    def __init__(self):
        self._list = []
    
    def add(self, key, data):
        i = 0
        #Creates a 2D array with 1 column and 2 rows [[0][0]]
        rows, cols = (1,2)
        newList = [[0]*cols]*rows
        
        #Checks if the key is an integer and that the key is not negative
        if isinstance(key,int) == True and key>=0:
            #Sets values in newList to key and data
            newList[0][0] = key
            newList[0][1] = data
            
            #Runs if there is no elements in self._list and appends newList to self._list
            if len(self._list) == 0:
                self._list.append(newList)

            #There are elements in self._list
            else:
                #Looks for the position that the key and data needs to be inserted
                while (self._list[i][0][0] < key):
                    i+=1
                    #Breaks the loop if the elements are being added at the end of the list
                    if i == len(self._list):
                        break

                #Inserts the elements to the right position in the list
                self._list.insert(i, newList)

    def min(self):
        return (self._list[0][0][0],self._list[0][0][1])

    def remove_min(self):
        rmin = self._list.pop(0)
        return(rmin[0][0], rmin[0][1])
        
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._list)