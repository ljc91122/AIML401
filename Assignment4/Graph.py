import numpy as np


class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, e):
        self.list.append(e)

    def dequeue(self):
        x = self.list[0]
        self.list.pop(0)
        return x
    def is_empty(self):
        return len(self.list)==0

class Stack:
    def __init__(self):
        self.list=[]

    def push(self,e):
        self.list.append(e)

    def pop(self):
        x= self.list[-1]
        self.list.pop()
        return x

    def is_empty(self):
        return len(self.list)==0

class Node:
    def __init__(self,data):
        self.data=data
class Graph:
    def __init__(self,n):
        self.n=n
        self.nodelist=[]
        self.adjmat=np.zeros((n,n))
        for i in range(n):
            self.nodelist.append(Node(i))

    def set_edge(self,source,destination,weight):
        self.adjmat[source, destination]= weight
        self.adjmat[destination,source]= weight

    def BFS(self,start):
        visited=np.zeros(self.n)
        q=Queue()
        q2=Queue()
        q.enqueue(self.nodelist[start])
        q2.enqueue(start)
        while not q.is_empty():
            print(q.dequeue().data)
            current=q2.dequeue()
            visited[current] = 1
            for i in range(self.n):
                if (self.adjmat[current,i] == 1) and (visited[i] == 0):
                    visited[i]=1
                    q.enqueue(self.nodelist[i])
                    q2.enqueue(i)

    def DFS(self,start):
        visited=np.zeros(self.n)
        s=Stack()
        s2=Stack()
        s2.push(start)
        s.push(self.nodelist[start])
        while not s.is_empty():
            current=s2.pop()
            visited[current]=1
            print(s.pop().data)
            for i in range(self.n):
                if (self.adjmat[current, i] == 1) and (visited[i] == 0):
                    visited[i] = 1
                    s.push(self.nodelist[i])
                    s2.push(i)

    def Dijkstra(self,source):
        self.source=source
        pre=np.zeros(self.n)
        shortest_path = [np.Inf for i in range(self.n)]
        shortest_path_flag = np.zeros(self.n)
        shortest_path[source]=0
        shortest_path_flag[source]=1
        for i in range(self.n):
            if self.adjmat[source,i] != 0:
                shortest_path[i]=self.adjmat[source,i]

        for i in range(self.n-1):
            idx=0
            smallest_value=np.inf
            for j in range(self.n):
                if shortest_path_flag[j] == 0 and  shortest_path[j] < smallest_value:
                        smallest_value=shortest_path[j]
                        idx=j
            for j in range(self.n):
                if self.adjmat[idx,j] != 0 and shortest_path[idx] + self.adjmat[idx,j] < shortest_path[j]:
                    shortest_path[j] = self.adjmat[idx,j] + shortest_path[idx]
                    pre[j]=idx
        return shortest_path



if __name__=='__main__':
    g=Graph(4)
    g.set_edge(0,1,1)
    g.set_edge(0,2,2)
    g.set_edge(0,3,1)
    g.set_edge(1,2,2)

    print(g.Dijkstra(0))
