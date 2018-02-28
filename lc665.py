class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        def check(nums,flag):
            if nums==[]:
                return True
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i]:
                    if flag == 0:
                        sub1=list(nums)
                        del sub1[i]
                        sub2=list(nums)
                        del sub2[i+1]
                        return check(sub1,1) or check(sub2,1)
                    else:
                        return False
            return True
               
            
        return check(nums,0)
                           
        