In this assigment you are required to rewrite the preorder, inorder and postorder Depth-first Traversal methods of a binary tree
class using stack.

Hints: You will need a Stack class for this.

Here is the pseudo-codes for the inorder DFS for your reference:

***Inorder DFS***

```
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current.left until current is None
4) If current is None and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item.right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.

```

