def recursiveRange(num):
    if num == 0:
        return 0
    return num + recursiveRange(num - 1)


if __name__ == '__main__':
    print(recursiveRange(10))