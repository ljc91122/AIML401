class MyIntegerListBase:
    def __init__(self):
        self.list=[]

    def get_n(self):
        return len(self.list)

    def add_number(self,num):
        self.num=num
        if isinstance(self.num,int):
            self.list.append(num)
        return self.list


    def delete_number(self):
        self.list.pop()


class MyIntegerList(MyIntegerListBase):


    def get_list(self):
        return self.list


    def binary_search(self, num, low, high):
        self.num=num
        self.low=low
        self.high=high

        if low > high:
            return -1
        else:
            mid = (low + high) // 2
            if num == self.list[mid]:
                return mid
            elif num < self.list[mid]:
                return self.binary_search(num, low, mid - 1)
            else:
                return self.binary_search(num , mid + 1, high)

if __name__=='__main__':
     my=MyIntegerList()
     my.add_number(1)
     my.add_number(3)
     my.add_number(4)
     my.add_number(6)
     my.add_number(6)
     my.add_number(7)
     my.add_number(8)
     my.add_number(9)
     my.delete_number()
     print(my.binary_search(9,0,6))
