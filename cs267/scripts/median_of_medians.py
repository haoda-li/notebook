# --8<-- [start:mom]
def select(arr, k):
    """ find the kth smallest element in arr
    """

    # divide arr into chunks of 5 elements, and sort each chunk
    # O(n) time, each sort on O(1) elements with O(n/5) arrs
    chunks = [
        sorted(arr[i: i+5]) 
        for i in range(0, len(arr), 5)
    ] 
    medians = [chunk[len(chunk) // 2] for chunk in chunks]

    # O(n/5) size recursive call
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select(medians, len(medians) // 2)

    # O(n) time
    p = partition(arr, pivot)

    # recursion depends on the position of pivot
    if k == p:
        return pivot
    if k < p:
        # O(7n/10) recursive
        return select(arr[0:p], k)
    else:
        # O(7n/10) recursive
        return select(arr[p+1:len(arr)], k - p - 1)


def partition(arr, pivot):
    """ Two pointers implementation of 
    partition. partition the arr such that
    arr[i] < pivot for all i < p
    arr[i] >= pivot for all i > p
    """
    left, right = 0, len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left
# --8<-- [end:mom]

arr = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
pivot = select(arr, len(arr) - 1)
print(pivot)
