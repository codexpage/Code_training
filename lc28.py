class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)  #imlement it, not call func
        
        #this is the most naive method, but faster than find()???
        n=len(needle)
        h=len(haystack)
        if h<n:
            return -1
        for i in range(h-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
    
        #better method is KMP, comlexity is worst O(2*len(haystack))
        