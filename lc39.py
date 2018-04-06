#这个就是dfs，但是分支数不确定，要用循环来确定
class Solution:
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort(reverse=True)
        return search(nums,target)
def search(nums, target):
    num = nums[0]
    # print(nums,target)
    if len(nums)==1:
        if target%num==0:
            return [[num]*(target//num)]
        else:
            return []  
    amount = target//num #could be 0
    res=[]
    for i in range(amount+1):
        sub = search(nums[1:],target-(i*num))
        res += [[num]*i+li for li in sub]
    return res
        
            
        
        