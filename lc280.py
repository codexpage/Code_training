
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = 1
        for i in range(len(nums)-1):
            # print(flag,nums[:i+2])
            if flag:
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            else:
                if nums[i]<nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            flag = 1-flag
                
        