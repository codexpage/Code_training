class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        row = [1,1]
        alllist=[[1],[1,1]]
        for j in range(numRows-2):
            nextrow =[]
            for i in range(len(row)-1):
                nextrow.append(row[i]+row[i+1])
            nextrow.insert(0,1)
            nextrow.append(1)
            row=nextrow
            alllist.append(row)
        return alllist
        