def heap_sorte():
    l = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]
    l = l[::-1]
    for i in l:
        for j in i:
            if i % 2 > 0 and l[i][j] > l[i+1][j]:
                l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
                l = l[1::]
                for k in i:
                    if k > k+1:
                        l[i][k], l[i+1][k] = l[i+1][k], l[i][k]
                    else:
                        l[i][k+1], l[i+1][k] = l[i+1][k], l[i][k+1]
            else:
                for w in i:
                    if k > k+1:
                        l[i][w], l[i+1][w] = l[i+1][w], l[i][w]
                    else:
                        l[i][w+1], l[i+1][w] = l[i+1][w], l[i][w+1]
    return l


def buildMaxHeaporg(arr, n):
    for i in reversed(range(n)):
        # print(i)
        # if child is bigger than parent
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i
            # swap child and parent until
            # parent is smaller
            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j],
                 arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],
                                           arr[j])
                j = int((j - 1) / 2)


def buildMaxHeap(arr, n):
    for i in reversed(range(n)):
        # print(i)
        # if child is bigger than parent
        while arr[i] > arr[int((i - 1) / 2)]:
            (arr[i],
             arr[int((i - 1) / 2)]) = (arr[int((i - 1) / 2)],
                                       arr[i])
            i = int((i - 1) / 2)


def heap_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        buildMaxHeap(arr, n)
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n = n-1
        # print(arr)


arr = [10, 20, 15, 17, 9, 21, 30]
n = len(arr)
print(arr)
heap_sort(arr)
print(arr)
