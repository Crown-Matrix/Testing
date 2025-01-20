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
    def IndexOf(self,data):
        """
        Returns index of first occurence in list
        """
        if self.length == 0:
            return "List Empty"
        current_node = self.head.next
        counter = 0
        while current_node != None and current_node.data != data:
            counter += 1
            current_node = current_node.next
        if current_node == None:
            return "Data Not Found In List"
        return counter
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

pass