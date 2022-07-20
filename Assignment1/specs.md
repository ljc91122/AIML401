# MyIntegerList class and binary search

In this assigment you are required to implement two classes named **MyIntegerListBase** and
**MyIntegerList**.
The **MyIntegerListBase** class (base-class) should be inherited by **MyIntegerList** class (sub-class).

**MyIntegerListBase** class implements the basic functions of an integer list, e.g. store a list whose elements should only be integers, store the length of a list, etc.
Here are the properties and methods you should implement:

```
Properties:

list: #Python list, the container of the integer list
n: #integer, length of the list
```

```
Methods:

constructor: # the parameter it takes is a python list object, if no prameter is given, the an empty list should be created.
get_n(): # get the length of the list, should be zero if it is a empty list.
add_number(num): # add one integer to the end of the list. You should check if the given parameter is a valid integer or not. If not then ignore. Update n.
delete_number(): # delete the last entry of the list. Update n.
```

**MyIntegerList** class inherits the above class by adding additional method called binary_search(num, low, high):

binary_search implements the binary search algorithm in a recursive way (it calls itself).
The function takes 3 integers as the parameters: target number, low and high indices for consideration. It gives the index of the target number if it exists in the list or -1 if not.

```
Example use case:

mylist = MyIntegerList([1,3,4,6,6,7,8])
mylist.binary_search(4,0,6)
# The output should be 2

mylist.binary_search(2,0,6)
# The output should be -1

mylist.add_number(9)
mylist.binary_search(9,0,7)
# The output should be 7

mylist.delete_number()
mylist.binary_search(9,0,6)
# The output should be -1
```





