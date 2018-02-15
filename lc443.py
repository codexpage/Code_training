class Solution:
    def compress(self, s):
        """
        :type chars: List[str]
        :rtype: int
        """
        if s==[]:
            return 0
        res=[]
        count=1
        for index in range(len(s)):
            char=s[index]
            if index == len(s)-1:
                res.append(char)
                if count!=1:
                    res.extend(list(str(count)))
            elif s[index+1]==s[index]:
                count+=1
            else:
                res.append(char)
                if count!=1:
                    res.extend(list(str(count)))
                count=1
        if len(res)<=len(s):
            s.clear()
            s.extend(res)
            return len(s)
        else:
            return len(s)