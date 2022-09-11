def insertion_sorting(x):
    n=len(x)
    for i in range(1,n):
        temp=x.pop(i)
        for j in range(i+1):
            if temp < x[j] or j==i:
                x.insert(j,temp)
                break

def bubble_sorting(x):
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp

def selection_sorting(x):
    for i in range(len(x)):
        minimum = i
        for j in range(i + 1, len(x)):
            if (x[j] < x[minimum]):
                minimum = j
        temp = x[i]
        x[i] = x[minimum]
        x[minimum] = temp
    return x

def merge_sorting(x):

    if len(x) > 1:
        a = len(x)//2
        l = x[:a]
        r = x[a:]
        merge_sorting(l)
        merge_sorting(r)
        b = c = d = 0

        while b < len(l) and c < len(r):
            if l[b] < r[c]:
                x[d] = l[b]
                b += 1
            else:
                x[d] = r[c]
                c += 1
            d += 1

        while b < len(l):
            x[d] = l[b]
            b += 1
            d += 1

        while c < len(r):
            x[d] = r[c]
            c += 1
            d += 1

def partition(array, low, high):
    pivot = array[low]
    x = low + 1
    y = high

    while True:
        while x <= y and array[y] >= pivot:
            y = y - 1
        while x <= y and array[x] <= pivot:
            x = x + 1
        if x <= y:
            array[x], array[y] = array[y], array[x]
        else:
            break
    array[low], array[y] = array[y], array[low]
    return y

def quick_sorting(array, low, high):
    if low >= high:
        return

    p = partition(array, low, high)
    quick_sorting(array, low, p-1)
    quick_sorting(array, p+1, high)

x=[2,3,8,1,9,3,4,6]
# insertion_sorting(x)
# selection_sorting(x)
# bubble_sorting(x)
# merge_sorting(x)
# quick_sorting(x,0,len(x)-1)
print(x)