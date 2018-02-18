class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        if "" in strs:
            return ""
        ch=strs[0][0]
        leng = min(strs)
        prefix = ""
        for i in range(len(leng)):
            ch = strs[0][i]
            for s in strs:
                if s[i]!=ch:
                    return prefix
            prefix +=ch
        return prefix
            
        