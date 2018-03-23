#这题主要难在分情况讨论，情况分的不好，就很难写，很容易漏掉相等的情况。

#这种方法情况分的很不好，写就花了好久，debug又好久
#和最后一个元素比较，前半截都大于最后一个元素，后半截都小于最后一个元素
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return -1
        
#         left = 0
#         right = len(nums)-1
#         last = nums[-1]
#         while left<= right:
#             mid = (left+right)//2
#             # print(left,mid,right)
#             if nums[mid]==target:
#                 return mid
#             elif target>nums[mid]:
#                 if target<=last:
#                     left = mid+1
#                 else:
#                     if nums[mid]<last:
#                         right = mid-1
#                     else:
#                         left = mid+1     
#             else:
#                 if target<=last:
#                     if nums[mid]>last:
#                         left = mid+1
#                     else:
#                         right = mid-1
#                 else:
#                     right = mid-1
#         return -1
                    
#更好的想法：
#(left,mid,right)
#比较left和mid的大小。左半边顺序正常left<mid，说明分界点在右半截，
#如果left<target<mid 说明在左半边，否则在右半边
#当left>mid的时候，左半边顺序顺序不对，说明分界点在左半截，那么右半边顺序正常
#如果mid<target<right 说明在右半边，否则在左半边


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left<=right:
            mid=(left+right)//2
            # print(left,mid,right)
            if nums[mid]==target:
                return mid
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


                    