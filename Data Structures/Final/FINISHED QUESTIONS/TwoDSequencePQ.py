from PriorityQueue_Interface import PriorityQueue_Interface

class TwoDSequencePQ(PriorityQueue_Interface):
    def __init__(self):
        self._list = []
    
    def add(self, key, data):
        i = 0
        #Checks if the key is an integer and that the key is not negative
        if isinstance(key,int) == True and key>=0:
            
            #Runs if there is no elements in self._list and appends the key and data to the end of the list
            if len(self._list) == 0:
                self._list.append((key,data))

            #There are elements in self._list
            else:
                #Looks for the position that the key and data needs to be inserted
                while (self._list[i] < key):
                    i+=1
                    #Breaks the loop if the elements are being added at the end of the list
                    if i == len(self._list):
                        break

                #Inserts the elements to the right position in the lists
                #self._data.insert(i, data)
                self._list.insert(i, (key,data))

    def min(self):
        return (self._list[0])#, self._data[0])

    def remove_min(self):
        return(self._list.pop(0))#,self._data.pop(0))
        
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._list)

#python TwoDSequencePQTester.py