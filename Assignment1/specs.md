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

constructor: # the parameter it takes is a python list object, if no parameter is given, then an empty list should be created.
get_n(): # get the length of the list, should be zero if it is an empty list.
add_number(num): # add one integer to the end of the list. You should check if the given parameter is a valid integer or not. If not then ignore. Update n.
delete_number(): # delete the last entry of the list. Update n.
```

**MyIntegerList** class inherits the above class by adding two additional methods called binary_search_main(num) and binary_search(num, list):

binary_search_main(num) takes one integer as the parameter, it gives the index of the number if it exists in the list or -1 if not. It calls a recursive funciton binary_search(num,list) which takes two parameters: an integer and a python list. 

binary_search(num, list) implements the binary search algorithm in a recursive way (it calls itself).


```
Example use case:

mylist = MyIntegerList([1,3,4,6,6,7,8])
mylist.binary_search_main(4)
# The output should be 2
mylist.binary_search_main(2)
# The output should be -1
mylist.add_number(9)
mylist.binary_search_main(9)
# The output should be 7
mylist.delete_number()
mylist.binary_search_main(9)
# The output should be -1
```





