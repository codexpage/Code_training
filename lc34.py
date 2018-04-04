#这里是用了两次二分搜索，一次搜左边界，一次右边界，当然是很正确的方法
#不过还可以用二分式的区间搜索，更偏向divide and concoqer，搜索整个list中的区间=左半边的区间+右半边的区间 拼起来
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=[float("-inf")]+nums+[float("inf")]
        left = self.findpos(nums,target,"left")
        right = self.findpos(nums,target,"right")
        return [left-1 if left!=-1 else -1, right-1 if right!=-1 else -1]

    
    def findpos(self, nums, target, border):
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                if border == "left":
                    if nums[mid]>nums[mid-1]:
                        return mid
                    else:
                        right=mid-1
                else:
                    if nums[mid]<nums[mid+1]:
                        return mid
                    else:
                        left=mid+1  
            elif nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        return -1
        
            
        