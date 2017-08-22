# Quick sort uses divide and conquer.
# The base case would be to determine when the array is size 1 or less or anything under 2, no need to sort it.


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # set the pivot to the first item
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) # recursive call with combined result


if __name__ == '__main__':
    arr = [8, 4, 2, 7, 3, 1, 5, 9, 10, 2]
    print(quicksort(arr))
