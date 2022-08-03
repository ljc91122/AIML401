class Queue:
    def __init__(self,shares,price):
        self.shares=[]
        self.price=[]

    def enqueue(self,shares,price):
        self.shares.append(shares)
        self.price.append(price)

    def return_queue(self):
        return self.shares,self.price

    def dequeue(self):
        return self.shares.pop(0)

    def sell(self,new_price,shares_sold):
        q=self.shares.pop(0)
        a=self.price.pop(0)
        y=self.shares.pop(0)
        b=self.price.pop(0)
        z=self.shares.pop(0)
        c=self.price.pop(0)
        return q * (new_price - a) + y * (new_price - b) + ((shares_sold - q - y) * (new_price - c))



#for stack question when there is an operator use the last two numbers

if __name__=='__main__':
    q=Queue(0,0)
    q.enqueue(100,20)
    q.enqueue(20,24)
    q.enqueue(200,36)
    print(q.sell(30,150))
