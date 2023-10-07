def get_diagonal(tup):
    list1 = [j[i] for i, j in enumerate(tup)]
    return tuple(list1)

if __name__ == '__main__':
    input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    print(get_diagonal(input_tuple))