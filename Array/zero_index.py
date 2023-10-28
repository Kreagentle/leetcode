class Solution(object):
    def moveZeroes(self, nums):
        zeroIndex = -1
        for i, el in enumerate(nums):
            if el == 0 and zeroIndex == -1:
                zeroIndex = i
            elif zeroIndex != -1:
                nums[zeroIndex] = el
                nums[i] = 0
                while zeroIndex < len(nums) - 1 and nums[zeroIndex] != 0:
                    zeroIndex += 1

        return nums