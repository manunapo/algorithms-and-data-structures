def moveRight(to, fro, arr):
    arr.insert(to, arr.pop(fro))


def insertionSort(n, arr):
    for i in range(1, n):
        newPos = None
        for j in reversed(range(0, i)):
            if arr[i] < arr[j]:
                newPos = j
            else:
                break
        if newPos != None:
            moveRight(newPos, i, arr)
        print(arr)
    return (arr)


def quicksort(arr):
    toR = []
    if len(arr) == 1:
        toR.append(arr[0])
    elif len(arr) > 1:
        pivot = arr[0]
        left = []
        right = []
        for e in arr[1:]:
            if e <= pivot:
                left.append(e)
            else:
                right.append(e)
        toR.extend(quicksort(left))
        toR.append(pivot)
        toR.extend(quicksort(right))
    return toR
