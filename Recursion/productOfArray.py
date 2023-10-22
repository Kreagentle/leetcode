def productOfArray(arr):
    if len(arr) == 0:
        return 1
    if len(arr) == 1:
        return arr[0]
    return arr[0] * productOfArray(arr[1:])

if __name__ == '__main__':
    print(productOfArray([1,2,3,10]))