#这个方法还是很套路的，要记住

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i,v in reversed(list(enumerate(nums))):
            if i==0:
                nums.reverse()
                return
            if nums[i-1]<nums[i]:
                target = i-1
                for j in range(i,len(nums)):
                    newtarget=None
                    # print(nums[j])
                    if nums[j]<=nums[target]:
                        newtarget=j-1
                        # print("newtraget",newtarget)
                    elif j==len(nums)-1:
                        newtarget=j
                    if newtarget:
                        # print(nums[target],nums[newtarget])
                        nums[target],nums[newtarget]=nums[newtarget],nums[target]
                        nums[target+1:]=reversed(nums[target+1:])
                        return
                    
            
        
        