#It'a hard problem to think and take me long time to write because not being familar with sort cmp func
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums): #all zero corner case 
            return "0"  #not "000"
        return "".join([str(e) for e in sorted(nums, cmp=self.compare)])
    def compare(self, a,b):
        return int(str(b)+str(a)) - int(str(a)+str(b))