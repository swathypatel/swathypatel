


# 75. Sort Colors
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)): # [2,0,2,1,1,0]
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        for k in range(len(nums)):
            if nums[k] == 1:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1