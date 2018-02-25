class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==[]:
            return []
        return self.getperm(nums)
        
    def getperm(self,nums):
        # print(nums)
        if len(nums)==1:
            return [nums]
        
        reslist = []
        for ch in nums:
            subnums = list(nums)
            subnums.remove(ch)
            sublist = self.getperm(subnums)
            reslist.extend([ch]+l for l in sublist)
            # print(reslist)
        return reslist 