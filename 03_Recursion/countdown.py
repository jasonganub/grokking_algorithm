# Every recursion solution requires a base case and a recursive case.
def countdown(i):
    print i
    if i <= 0:
        return
    else:
        countdown(i-1)


if __name__ == '__main__':
    countdown(10)