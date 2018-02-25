#different from normal perm(), I make use of set() uniqueness 
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==[]:
            return []
        return [list(x) for x in set(tuple(x) for x in self.getperm(nums))]
        
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
        