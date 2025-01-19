Linked List Implementation Module

supports zero-based indexing
head node is not given any data value

Methods:
Append(data)
 -Takes data argument and creates node with data and appends at end of list


Prepend(data)
-Takes data argument and creates node with data to prepend at beginning of list


printList()
-Prints all data on list on new lines


deleteIndex(index)
 -deletes node at given index


IndexInsert(index,data)
-creates node at new index(moving old one aside if any)
-can prepend or create first node


deleteIndex(index)
-deletes node at given index


convert_to_list()
-returns list containing linked list node values
-returns empty list if linked list is empty


mapFunction(func,*args)
-runs given func on each list node with node value as main parameter and any side parameters can be accepted as well


ProtectedMapFunction(func,*args)
-the protected version will continue to iterate through the linked list despite any raised exception from the function call
-any individiaul node with a raised exception will not have their value changed

length(attribute)
--linked_list object keeps track of length without needing to iterate through list



ToBeAdded:

ReplaceAtIndex(index,data)
--Replaces node at index with a new node with given data


clear()
-Disconnects all nodes from head

filter(func)
-Uses given function argument as True/False key to decide to delete/keep each node