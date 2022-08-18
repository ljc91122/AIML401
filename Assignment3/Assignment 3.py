class Stack:
    def __init__(self):
        self.list=[]

    def push(self,e):
        self.list.append(e)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list)==0

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinaryTree:
    def __init__(self,root):
        self.root=root

    def get_root(self):
        return self.root

    def add_left(self,currenct,data):
        n=Node(data,None,None)
        currenct.left=n
        return n

    def add_right(self,currenct,data):
        n=Node(data,None,None)
        currenct.right=n
        return n

    def inorder(self):
        current=self.root
        stack=Stack()
        while True:
            if current is not None:
                stack.push(current)
                current=current.left
            elif(stack):
                current=stack.pop()
                print(current.data)
                current=current.right
            else:
                break



    def postorder(self):
        stack=[]
        stack.append(self.root)
        stack2=[]

        while stack:
            current=stack.pop()
            stack2.append(current.data)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        while stack2:
            print(stack2.pop())


    def preorder(self):
        s=[]
        s.append(self.root)

        while s:
            current=s.pop()
            print(current.data)
            if current.right:
                s.append(current.right)
            if current.left:
                s.append(current.left)




if __name__=='__main__':
    bt=BinaryTree(Node(1))
    n=bt.add_left(bt.get_root(),2)
    bt.add_left(n,4)
    bt.add_right(n,5)
    n=bt.add_right(bt.get_root(),3)
    n=bt.add_left(n,6)
    bt.add_right(n,7)
    bt.postorder()
