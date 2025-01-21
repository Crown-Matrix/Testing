class node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

        
class linked_list():
    def __init__(self):
        self.head = node(data=None,next=None)
        self.length = 0
    def append(self,data):
        new_node = node(data=data)
        current_node = self.head
        if self.head.next == None:
            self.head.next = new_node
            self.length += 1
            return
        while current_node.next != None:
            current_node = current_node.next
        #at this point current_node = last node
        current_node.next = new_node
        self.length += 1
    

    
    def prepend(self,data):
        new_node = node(data=data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1
    
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
                self.length += 1
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
        self.length += 1
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
        if self.length == 0:
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
        if self.length == 0:
            return False
        current_node = self.head.next
        while current_node != None and current_node.data != data:
            current_node = current_node.next
        if current_node == None:
            return False
        return True
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    def clear(self):
        self.head.next = None
        self.length = 0
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
        Methods:
        1. All Occurences
        2. First Occurence
        3. Last Occurence
        Default method is #1
        Returns index of occurence(s) as result
        Returns "data not found in list" when no occurences found
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
pass