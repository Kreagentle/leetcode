def common_elements(tuple1, tuple2):
    return tuple([i for i in tuple1 if i in tuple2])

if __name__ == '__main__':
    print(common_elements((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))