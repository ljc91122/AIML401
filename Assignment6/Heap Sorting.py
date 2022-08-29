def heapify(arr, n, i):
    largest = i
    left_child_i = 2 * i
    right_child_i = 2 * i + 1
    if left_child_i < n and arr[i] < arr[left_child_i]:
        largest = left_child_i

    if right_child_i < n and arr[largest] < arr[right_child_i]:
        largest = right_child_i

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

x=[2,3,8,1,9,3,4,6]
heapSort(x)
print(x)