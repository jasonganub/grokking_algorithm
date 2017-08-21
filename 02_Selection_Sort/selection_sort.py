# A method to find the smallest element index in an array and to return it.
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# The implementation of the selection sort which is O(n^2) runtime.
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr



if __name__ == '__main__':
    arr = [2, 5, 7, 8, 4, 6, 3, 2, 1, 6, 9, 10, 4, 6]
    print(selection_sort(arr))