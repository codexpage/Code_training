#没什么思考的，就是很繁琐的，注意坐标规律

class Solution:
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if n==1:
            return s
        res=[]
        for i in range(n):
            if i==0 or i==n-1:
                self.addv(res,s,n,i,case=1)
            else:
                self.addv(res,s,n,i,case=2)
                # self.addv(res,s,n,(2*n-2)-i)
        return ''.join(res)
    def addv(self, res, s, n, i, case=1):
        secondpos = (2*n-2)-i
        while i<len(s):
            res.append(s[i])
            # print(i,s[i])
            if case==2 and secondpos<len(s):
                res.append(s[secondpos])
                # print('2:',secondpos,s[secondpos])
            i+=2*n-2
            secondpos+=2*n-2
 
            # x%(2*n-2)
        
        