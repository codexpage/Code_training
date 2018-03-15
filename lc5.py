#这个解法就是遍历所有中心和offset，复杂度O(n^2)
#但是不知道是不是写复杂了。 manacher算法O(n)显然要快很多

import math
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        oldstr=s
        newstr = ['#']*(2*len(s)+1)
        # newstr[0]='$'
        newstr[1::2]=s
        s = "".join(newstr)
    
        maxl = 0
        maxs = ""
        # lengs=[]
        for i in range(len(s)):
            leng = 0
            for offset in range(1,len(s)):
                if 0<= i-offset and i+offset <= len(s)-1:
                    if s[i-offset]==s[i+offset]:
                        # print(s[i-offset],s[i],s[i+offset],leng+1)
                        leng+=1
                    else:
                        break
            leng=(leng//2)*2 + (0 if s[i]=='#' else 1)
            # lengs.append(leng)
            if leng>maxl:
                maxs=s[i-(leng-1):i+(leng-1)+1]
                maxl=leng
        # print(s)
        # print("".join([str(x) for x in lengs]))
        return ''.join([s for s in maxs if s!='#'])
            
            
                        
                        
                    