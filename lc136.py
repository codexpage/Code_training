#非常巧妙，不知道基本想不到
#xor操作是可交互的，而且A xor A =0,知道这两点就很显然了

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res ^=num
        return res
        