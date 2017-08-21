# O (log n) because it splits every time which is very scalable

def binary_search(list, x):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2 # split in half for mid point
        guess = list[mid]
        if guess == x:
            return mid
        elif guess < x:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(binary_search(list, 8))
