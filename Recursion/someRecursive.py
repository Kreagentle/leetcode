def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    return someRecursive(arr[1:], cb)


if __name__ == '__main__':
    print(someRecursive([4,6,8], isOdd))