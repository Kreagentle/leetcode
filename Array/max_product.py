def max_product(arr):
    max1, max2 = arr[0], arr[0]

    for n in arr:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    return max1 * max2

if __name__ == '__main__':
    arr = [1, 7, 3, 4, 9, 5]
    print(max_product(arr))