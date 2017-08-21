# A good example of a recursion function for factorials
# ex: factorial(4) is 4! which is 4 * 3 * 2 * 1 = 24

def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)


if __name__ == '__main__':
    print(fact(4))