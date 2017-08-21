# Exercise 4.3 says to write a recursive function to find the max value in a list
def max_num(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    else:
        sub_max = max_num(list[1:])
        if list[0] > sub_max:
            return list[0]
        else:
            return sub_max

if __name__ == '__main__':
    list = [1, 4, 6, 3, 2, 7, 10, 3, 5]
    print(max_num(list))