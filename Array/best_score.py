def first_second(my_list):
    max1, max2 = my_list[0], my_list[0]

    for n in my_list:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n

    return max1, max2

if __name__ == '__main__':
    myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
    print(first_second(myList))