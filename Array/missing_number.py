def missing_number(arr, n):
    exp_sum = n * (n+1) // 2
    actual_sum = sum(arr)
    return exp_sum - actual_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(missing_number([1, 2, 3, 4, 6], 6))