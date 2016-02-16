from operator import lt

# two sorted lists
def merge(left, right, compare):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result

def mergeSort(L, compare = lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right, compare)
