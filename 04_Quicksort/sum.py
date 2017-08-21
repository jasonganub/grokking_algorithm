# Add all the numbers and return the total
# This is the iterative way
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

def recursive_sum(arr):
    # base case
    if arr ==  []:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])


if __name__ == '__main__':
    list = [2, 4, 6]
    print(recursive_sum(list))