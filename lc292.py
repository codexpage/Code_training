#nim博弈问题是可以规律的
#不需要min-max搜索
#3以内必赢，4必输，可以推出5,6,7必赢，那么8必输，以此类推，发现规律3赢1输的循环
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0:
            return False
        else:
            return True
        
        