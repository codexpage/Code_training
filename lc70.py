#This is fibonacci, how clever 
#I origially though this is infinite knapsack, DP, yes it is, and acturally 
#every term rely on the previous two term, c[i] = c[i-1]+c[i-2]
#so that is fibonacci!

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre2 = 1
        pre1 = 2
        for i in range(3,n+1):
            t = pre2+pre1
            pre2 = pre1
            pre1 = t
        return t 
            
            
        
        
        