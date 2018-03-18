
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        
        a[i]==b[j]
        dp[i][j]= dp[i-1][j-1]+1
        a[i]!=b[j]
        dp[i][j]=0
        """

        dp=[[0 for j in range(len(B))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=0
            
        return max([max(d) for d in dp])