# **Methods**

### Prepend(data)
-Adds given data to beginning of list

### Append(data)
-Adds given data to end of list

### PrintList()
-Prints List Out
-(line by line for each node)

### IndexData(index)
-Retrieves the data value from the node at the given index

### IndexInsert(index,data)
-Inserts a node at the given index with the given data

### DeleteIndex(index)
-Deletes the node at the given index

### convert_to_list()
-Returns linked list in regular list

### MapFunction(func,*args)
-for each item linked list, runs given function with the item as the main parameter
--Allows for more than 1 parameters
(only the first(main) parameter will be set to each item in the list)

### ProtectedMapFunction(func,*args)
-Protected means if any exception is rasied while running the given function with an item in the list, the exception will be ignored and continue looping through the list running the function on all items

### IndexOf(data,method)
-Returns index of occurence(s) of nodes with the given data.
Method:
1. First Occurence
2. Last Occurence
3. All Occurences (returns list)

### contains(data)
-Returns True/False for if the given data is within any of the nodes in the linked list

### isEmpty()
-Returns True/False for if the list is empty or not

### clear()
-Disconnects all nodes from head node

### length()
-Returns length of linked list
-Return 0 if empty

### RemoveLast()
-Deletes last item in list
-Returns data in the last item as a result
-Returns error if list is empty

### RemoveFirst()
-Removes first item in list
-Removes data of first item
-Returns an error if list is empty

### RemoveData(data,method)
-Removes occuence(s) of nodes with the given data in accordance to the specific type.
-Method:
1. All occurences
2. First Occurence
3. Last Occurence
-Returns index of occurence(s) as result
-Returns "data not found in list" when no occurences found

### Filter(func,*args)
-Iterates through linked list running given function with each node as input.
-Function should output True/False and will keep/delete a node in accordance.
-Returns index list of nodes removed
```python
def CheckIfFactor(num,factor):
    if num%factor == 0:
        return True
    else:
        return False
ll.Filter(CheckIfFactor,3)
#will only keep numbers dividable by 3
#any that arent will be removed from list
```

### CreateFromList(list)
-Returns a new linked list object with list values as node values

```python
a_regular_list = [1,2,3]    
a_linked_list = (linked_list.CreateFromList([a_regular_list]))
#the original regular list variable still exists, but the second variable has been assigned a new instance of the linked_list class with 1,2,3 as its first 3 values.
```

### ReplaceIndex(index,data)
-Replaces the node at the given index with a new node containing the given data

### ReplaceData(old_data,new_data,method)
-Replaces the nodes at specficiced occurence(determined by method) with a new node containing the given data
Methods:
1. All Occurences (returns list of occurence indexes)
2. First Occurence (returns index)
3. Last Occurence (returns index)

# **TO BE ADDED**
iterator():
-Returns iterable object class containing all __*current*__ values in list