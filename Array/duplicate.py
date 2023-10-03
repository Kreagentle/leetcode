def contains_duplicate(nums):
    arr = set()
    for i in nums:
        arr.add(i)
    if len(nums) != len(arr):
        return True
    return False

if __name__ == '__main__':
    print(contains_duplicate([1,2,3,1]))