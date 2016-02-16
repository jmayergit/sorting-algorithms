from random import randint

def buildArr(n):
    arr = []
    for i in range(n):
        arr.insert(0, randint(1,99))

    return arr


def selectSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        minVal = arr[minIndex]
        j = i + 1

        while j < len(arr):
            if minVal > arr[j]:
                minIndex = j
                minVal = arr[j]

            j += 1

        if minIndex != i:
            temp = arr[i]
            arr[i] = minVal
            arr[minIndex] = temp

    return arr
