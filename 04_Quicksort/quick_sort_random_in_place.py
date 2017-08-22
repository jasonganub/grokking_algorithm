# Quick sort uses divide and conquer.
# The base case would be to determine when the array is size 1 or less or anything under 2, no need to sort it.
# This one runs in place with a partition function

def quicksort_helper(arr):
    return quicksort(arr, 0, len(arr) - 1)

def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index - 1) # make sure one side is inclusive
    quicksort(arr, index, right)
    return arr

def partition(arr, left, right, pivot):
    # Returns index
    while left <= right:
        while arr[left] < pivot:
            left += 1 # if val is less than pivot, shift leftmark right

        while arr[right] > pivot:
            right -= 1 # if val is less than pivot, shift rightmark left

        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            # keep shifting, there may be more
            left += 1
            right -= 1
    return left


if __name__ == '__main__':
    arr = [8, 4, 2, 7, 3, 1, 5, 9, 10, 2]
    print(quicksort_helper(arr))
