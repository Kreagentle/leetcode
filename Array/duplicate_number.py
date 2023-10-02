def remove_duplicates(my_list):
    my_list.sort()
    if len(my_list) < 2:
        return my_list
    temp = len(my_list)
    i = 0
    while temp > i+1:
        if my_list[i] == my_list[i+1]:
            my_list.pop(i+1)
            i = 0
        else:
            i += 1
        temp = len(my_list)
    return my_list


if __name__ == '__main__':
    print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
