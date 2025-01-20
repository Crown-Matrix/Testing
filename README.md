### Methods

## Prepend(data)
-Adds given data to beginning of list

## Append(data)
-Adds given data to end of list

## PrintList()
-Prints List Out
-(line by line for each node)

## IndexData(index)
-Retrieves the data value from the node at the given index

## IndexInsert(index,data)
-Inserts a node at the given index with the given data

## DeleteIndex(index)
-Deletes the node at the given index

## convert_to_list()
-Returns linked list in regular list

## MapFunction(func,*args)
-for each item linked list, runs given function with the item as the main parameter
--Allows for more than 1 parameters
(only the first(main) parameter will be set to each item in the list)

## ProtectedMapFunction(func,*args)
Protected means if any exception is rasied while running the given function with an item in the list, the exception will be ignored and continue looping through the list running the function on all items

## IndexOf(data)
-Returns index of first occurence of given data in linked list

## contains(data)
-Returns True/False for if the given data is within any of the nodes in the linked list

## isEmpty()
-Returns True/False for if the list is empty or not

## clear()
-Disconnects all nodes from head node

### TO BE ADDED

## Filter(func,*args)

## RemoveLast()

## RemoveFirst()

## RemoveData(data,type)
types:
1. All occurences
2. First Occurence
3. Last Occurence

## Iterator()
returns generator object

## IndexOf(data,type)
Types:
1. First Occurence
2. Last Occurence


===========================================