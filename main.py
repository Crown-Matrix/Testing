class node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

        
class linked_list():
    def __init__(self):
        self.head = node(data=None)
    def append(self,data):
        new_node = node(data=data)
        current_node = self.head
        if self.head.next == None:
            self.head.next = new_node
            return
        while current_node.next != None:
            current_node = current_node.next
        #at this point current_node = last node
        current_node.next = new_node
    

    
    def prepend(self,data):
        new_node = node(data=data)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def printList(self):
        current_node = self.head.next
        if current_node == None:
            print ("List Empty")
            return
        while current_node != None:
            print (current_node.data)
            current_node = current_node.next
    def IndexData(self,index):
        if self.head.next == None:
            return "list is empty"
        current_node = self.head.next #starting at first real node to preserve 0-based indexing
        counter = 0
        while counter < index and current_node.next != None:
            counter += 1
            current_node = current_node.next
        if counter == index:
            return current_node.data
        else:
            return "Index Not Found"
    def IndexInsert(self,index,data):
        try:
            index = int(index)
        except:
            return "index input error"
        else:
            if index < 0:
                return "index input error"
        first_node = self.head.next
        target_index = index-1
        counter = 0
        current_node = first_node
        if self.head.next == None:
            if index == 0:
                self.head.next = node(data=data)
                return
            else:
                return "Index Error: Empty List"
        while target_index > counter and current_node.next != None:
            counter += 1
            current_node = current_node.next
        if current_node.next == None and target_index != counter:
            return "IndexError: Given Index Exceeds List Range"
        replaced_node = current_node.next
        current_node.next = node(data=data,next=replaced_node)
        return "Success"
    def deleteIndex(self,index):
        try:
            index = int(index)
        except:
            return "index input error"
        else:
            if index < 0:
                return "index input error"
        if self.head.next == None:
            return "Empty List"
        current_node = self.head
        counter = -1
        while counter < index and current_node.next != None:
            counter += 1
            previous_node = current_node
            current_node = current_node.next
        if current_node.next != None and counter != index:
            return "Index Error: index exceeds list range"
        previous_node.next = current_node.next
        return "Success"
        previous_node.next = current_node.next
    def convert_to_list(self):
        """
        returns a list containing elements of linked list
        returns empty list if linked list is empty
        """
        result = []
        current_node = self.head.next
        while current_node != None:
            result.append(current_node.data)
            current_node = current_node.next
        return result
    def mapFunction(self,func,*args):
        """
        *args include function object and any associated *args
        *changes are directly applied to each object in linked list
        """
        if type(func) != type(lambda:None):
            return "func paramater must be a callable function"
        current_node = self.head.next
        while current_node != None:
            current_node.data = func(current_node.data,*args)
            current_node = current_node.next
        return "success"
    def ProtectedMapFunction(self,func,*args):
        """
        *args include function object and any associated *args
        *changes are directly applied to each object in linked list

        Protected means each any raised exception will be ignored
        function arg will be ran on all list values regardless of exceptions
        """
        if type(func) != type(lambda:None):
            return "func paramater must be a callable function"
        current_node = self.head.next
        while current_node != None:
            try:
                current_node.data = func(current_node.data,*args)
            except:
                pass
            finally:
                current_node = current_node.next
        return "success"
    def IndexOf(self,data,method):
        """
        Returns index of occurence(s) in list
        Types:
        1. First Occurence
        2. Last Occurence
        3. All Occurences (returns list)
        """
        if self.head.next == None:
            return "List Empty"
        match method:
            case 1:
                current_node = self.head.next
                counter = 0
                while current_node != None and current_node.data != data:
                    counter += 1
                    current_node = current_node.next
                if current_node == None:
                    return "Data Not Found In List"
                return counter
            case 2:
                if self.head.next == None:
                    return "List Empty"
                current_node = self.head.next
                counter = 0
                indexes = []
                while current_node != None: 
                    if current_node.data == data:
                        indexes.append(counter)
                    counter += 1
                    current_node = current_node.next
                try:
                    return indexes[-1]
                except IndexError:
                    return "Data not in list"
                
            case 3:
                if self.head.next == None:
                    return "List Empty"
                current_node = self.head.next
                counter = 0
                indexes = []
                while current_node != None: 
                    if current_node.data == data:
                        indexes.append(counter)
                    counter += 1
                    current_node = current_node.next
                return indexes
            case _:
                return "Input Error: Given type must be 1 or 2"
        
    def contains(self,data):
        if self.head.next == None:
            return False
        current_node = self.head.next
        while current_node != None and current_node.data != data:
            current_node = current_node.next
        if current_node == None:
            return False
        return True
    def isEmpty(self):
        if self.head.next == None:
            return True
        else:
            return False
    def clear(self):
        self.head.next = None
    def RemoveLast(self):
        """
        Deletes last item in list
        Returns data in last item as result
        Will return error if List is empty
        """
        current_node = self.head.next
        if current_node == None:
            return "List Empty Error"
        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data
    def RemoveFirst(self):
        """
        Removes first item in list
        Returns data of first item
        Returns an error if list is empty
        """
        current_node = self.head.next
        if current_node == None:
            return "List Empty Error"
                
        self.head.next = None if current_node.next == None else current_node.next
        return current_node.data
    def RemoveData(self,data,method=1):
        """
        -Removes Occurence(s) of data in list depending on selected method

        -Returns index of occurence(s) as result

        Method definitions:
        1. All Occurences(Default)
        2. First Occurence
        3. Last Occurence
        
        """
        match method:
            case 1:
                current_node = self.head.next
                previous_node = self.head
                applicable = False
                counter = 0
                indexes = []
                while current_node != None:
                    if current_node.data == data:
                        previous_node.next = current_node.next #deleter
                        current_node = current_node.next
                        indexes.append(counter)
                        applicable = True
                    else:
                        previous_node = current_node
                        current_node = current_node.next
                    counter += 1
                if applicable:
                    return indexes
                return "data not found in list"
    
            case 2:
                current_node = self.head.next
                previous_node = self.head
                counter = 0
                while current_node != None:
                    if current_node.data == data:
                        previous_node.next = current_node.next #deleter
                        return counter
                    #if not a match continue updating variables
                    counter += 1
                    previous_node = current_node
                    current_node = current_node.next
                return "data not found in list"

            case 3:
                current_node = self.head.next
                previous_node = self.head
                counter = 0
                applicable = False
                while current_node != None:
                    if current_node.data == data:
                        #overwrite last match info with latest match info
                        current_match = current_node
                        previous_match = previous_node
                        counter_match = counter
                        applicable = True
                    counter += 1
                    previous_node = current_node
                    current_node = current_node.next
                if applicable:
                    previous_match.next = current_match.next #deleter
                    return counter_match
                return "data not found in list"
            case _:
                return "Input Error: Not valid method"
    def Filter(self,func,*args):
        """
        -Iterates through linked list running given function with each node as input.
        -Function should output True/False and will keep/delete a node in accordance.
        -Returns index list of nodes removed
        """
        current_node = self.head.next
        previous_node = self.head
        counter = 0
        indexes = []
        applicable = False
        while current_node != None:
            match func(current_node.data,*args):
                case True:
                    previous_node = current_node
                    current_node = current_node.next
                case False:
                    previous_node.next = current_node.next
                    current_node = current_node.next
                    indexes.append(counter)
                    applicable = True
                case _:
                    return f"FUNCTION ERROR: Given function did not output True/False after inputting the node at index {counter} with data {current_node.data}"
            counter += 1
        if applicable:
            return indexes
        return "success"
    def CreateFromList(given_list):
        new_linked_list = linked_list()
        current_node = new_linked_list.head
        for i in given_list:
            current_node.next = node(data=i)
            current_node = current_node.next
        return new_linked_list
    def ReplaceIndex(self,index,data):
        """
        -Replaces the nodes at index to  be replaced by a new node with the given data
        """
        try:
            index = int(index)
        except:
            return "Index Input Error"
        else:
            if index < 0:
                return "Index Input Error"
        counter = 0
        previous_node = self.head
        current_node = previous_node.next
        while counter != index and current_node.next != None:
            counter += 1
            previous_node = current_node
            current_node = current_node.next
        if counter != index:
            return "Index Error: Given Index Exceeds List Range"
        previous_node.next = node(data=data,next=current_node.next)
        return counter
    def ReplaceData(self,old_data,new_data,method):
        """
        -Replaces the nodes at specficiced occurence(determined by method) with a new node containing the given data

        Methods:
        1. All Occurences (returns list of occurence indexes)
        2. First Occurence (returns index)
        3. Last Occurence (returns index)
        """
        match method:
            case 1:
                if self.head.next == None:
                    return "List Empty!"
                current_node = self.head.next
                previous_node = self.head
                counter = 0
                applicable = False
                indexes = []
                while current_node != None:
                    if current_node.data == old_data:
                        applicable = True
                        indexes.append(counter)
                        current_node.data = new_data
                    previous_node = current_node
                    current_node = current_node.next
                    counter += 1
                if applicable:
                    return indexes
                return "Data not in list"
            case 2:
                if self.head.next == None:
                    return "List Empty!"
                current_node = self.head.next
                counter = 0
                while current_node != None:
                    if current_node.data == old_data:
                        current_node.data = new_data
                        return counter
                    current_node = current_node.next
                    counter += 1
                return "data not in list"
            case 3:
                if self.head.next == None:
                    return "List Empty!"
                current_node = self.head.next
                counter = 0
                while current_node != None:
                    if current_node.data == old_data:
                        current_match = current_node
                        current_counter = counter
                    current_node = current_node.next
                    counter += 1
                current_match.data = new_data
                return current_counter
    def length(self):
        current_node = self.head.next
        counter = 0
        while current_node != None:
            counter += 1 #counter at beginning of loop for 1-based indexing
            current_node = current_node.next
        return counter
    def sorter(self,func_key=None,method=1):
        """
        Sorts linked list using pythons built-in timsort
        Methods:
        1. Returns new instance of linked list with sorted data
        2. Directly changes the content of the given linked list instance
        returns linked_list object based on method
        """
        ll_list = self.convert_to_list()
        sorted_list = list(sorted(ll_list,key=func_key))
        
        match method:
            case 1:
                return linked_list.CreateFromList(sorted_list)
            case 2:
                current_node = self.head.next
                for i in sorted_list:
                    current_node.data = i
                    current_node = current_node.next
                return self
            case _:
                "Invalid method input"
        
    def BubbleSort(self):
        """
        linked_list sorter using bubble sort algorithin
        (repeatingly swaps value pairs that are in wrong order)
        """
        pass
        try:
            if self.head.next.next == None:
                return "List Empty!"
        except:
            return "list empty!"
        
        previous_node = self.head.next
        current_node = previous_node.next
        verified_node = previous_node
        counter = 0
        while True:
            applicable = True
            previous_node = verified_node
            current_node = verified_node.next
            while current_node != None:
                if current_node.data < previous_node.data:
                    counter += 1
                    current_node.data,previous_node.data = previous_node.data,current_node.data
                    previous_node = self.head.next
                    current_node = previous_node.next #resets the algorithin back at the beginning
                    #eventually the previous/current node will be set to the last node that was determined to not need a switch
                    applicable = False
                else:
                    verified_node = previous_node
                previous_node = previous_node.next
                current_node = current_node.next
            if applicable:
                print (counter)
                break
    def findMin(self,method):
            current_node = self.head.next
            latest_node = current_node
            while current_node != None:
                try:
                    current_data = float(current_node.data)
                    if current_data < latest_node.data:
                        latest_node = current_node
                    current_node = current_node.next
                except:
                    pass
            match method:
                case 1: # returns node
                    return latest_node
                case 2: # returns node data
                    return latest_node.data
                case _:
                    return "invalid method input"
            return latest_node.data
    def findMax(self,method):
            current_node = self.head.next
            latest_node = current_node
            while current_node != None:
                try:
                    current_data = float(current_node.data)
                    if current_data > latest_node.data:
                        latest_node = current_node
                    current_node = current_node.next
                except:
                    pass
            match method:
                case 1: #return node
                    return latest_node
                case 2: #return node data
                    return latest_node.data
                case _:
                    return "invalid method input"
    def SelectionSort(self):
        """
        Directly Changes linked_link instance using the SelectionSort Algorithim
        
        Doesnt Return Anything
        """
        if self.head.next == None:
            return "List Empty"
        elif self.head.next.next == None:
            return self.head.next
        latest_node = self.head.next
        while latest_node != None:
            current_node = latest_node
            lowest_found_node = current_node
            while current_node != None:
                if current_node.data < lowest_found_node.data:
                    lowest_found_node = current_node
                current_node = current_node.next
            lowest_found_node.data,latest_node.data = latest_node.data,lowest_found_node.data
            latest_node = latest_node.next

        
    def SplitList(self,method):
        """
        Splits linked list down middle

        The original list will not be changed

        if length is odd, the first half will be the bigger half

        Methods:
        1: Returns new linked list object containing data from the first half
        2: Returns new linked list object containing data from the second half
        """
        first_node = self.head.next
        if first_node == None or first_node.next == None:
            return "List Length must be at least 2!"
        match method:
            case 1:
                fast_counter = self.head.next
                slow_counter = self.head.next
                while fast_counter != None and fast_counter.next != None and fast_counter.next.next != None: ## floor divison by 2
                    fast_counter = fast_counter.next.next
                    slow_counter = slow_counter.next
                slow_counter.next = None #split the halves
                current_node = self.head.next
                new_list = linked_list()
                while current_node != None:
                    new_list.append(current_node.data)
                    current_node = current_node.next
                return new_list
            case 2:
                first_node = self.head.next
                if first_node.next.next == None:
                    new_list = linked_list()
                    new_list.append(first_node.next.data)    
                    return new_list
                fast_counter = first_node
                slow_counter = first_node
                while fast_counter != None and fast_counter.next != None: ## floor divison by 2
                    fast_counter = fast_counter.next.next
                    slow_counter = slow_counter.next
                result = slow_counter.next
                slow_counter.next = None #split the halves
                current_node = result
                new_list = linked_list()
                while current_node != None:
                    new_list.append(current_node.data)
                    current_node = current_node.next
                return new_list
            case _:
                "Invalid Method Input"
    def __iter__(self):
        def generator():
            curerent_node = self.head.next
            while curerent_node != None:
                yield curerent_node.data
                curerent_node = curerent_node.next
        return generator()



ll = linked_list.CreateFromList([1,5,2,6,5,4,10,5,2,104,23,1,9,8,3,12,13,10,5,12])
ll.printList()


def TimeItTests():
    from random import randrange
    from timeit import timeit
    from os import system
    def randomLinkedList():
        return linked_list.CreateFromList([randrange(0,99999999999) for i in range(300)])
    def TimeChecksies():
        testee = randomLinkedList()
        testee.BubbleSort()
    def TimeeeCheckser():
        testee = randomLinkedList()
        testee.SelectionSort()
    def TimsieesssChecka():
        testee = randomLinkedList()
        testee.convert_to_list().sort()
    apple = (timeit(stmt=TimeChecksies,number=100))
    bannana = (timeit(stmt=TimeeeCheckser,number=100))
    orange = (timeit(stmt=TimsieesssChecka,number=100))
    system("clear")
    print (f"Bubble Sort: {apple}(ran 100 times)\nSelection sort: {bannana}(ran 100 times)\nDefaultSort: {orange}(ran 100 times)")
pass