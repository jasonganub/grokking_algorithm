# Exercise 4.2 says to write a recursive function to count the number of items in a list
def count_items(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_items(arr[1:])

if __name__ == '__main__':
    # should print 10
    arr = [1, 2, 3, 4, 6, 7, 4, 3, 5, 11]
    print(count_items(arr))