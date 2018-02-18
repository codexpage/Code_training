#very simple navie method, but very fast

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        for i in range(n-1):
            s=self.count(s)
            print(s)
        return s
        
    def count(self,s):
        res =""
        letter = s[0]
        leng = 1
        for i in range(len(s)):
            if i == len(s)-1:
                res += (str(leng)+letter)
            elif s[i+1]==s[i]:
                leng +=1
            else:
                res += (str(leng)+letter)
                leng = 1
                letter = s[i+1]
        return res
                
            
        