1. Implement the Heap sort algorithm.

Note that you don't need a Binary Tree structure (with left and right child reference) for this task. You'll store the heap into a python list since it is a complete binary tree.

You can easily get access to the i-th node's parent index by using the following fomula:

```
Parent_i = floor(i/2)
```

The indices of left and right children of i-th node are calculated as:

```
left_child_i = 2*i
right_child_i = 2*i + 1
```

The MinimumHeap class is defined as following:

```
property:

heap: python list #used to store the heap

methods:

def __init__(x): #constructor turning a given list x into a minimum heap
def heapify(): #adjust heap to a valid minimum heap (parent is smaller than its children)
def sort(n): #heap sort and print the smallest n elements in ascending order

```