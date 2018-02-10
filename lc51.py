class Solution(object):
    solutions = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.solutions = []
        #first we need to calcualte a res[n] for each line queen's pos
        #then covert it into Matrix
        
        #use dfs
        #first line we have n choice, we need to traverse the list,
        #we choose x at fist step
        #second line we can not choose choises x,x+1,x-1
        #assume we are on line t, and the previos choice are [l1,l2,l3..lt-1]
        #for li we cannot choose offset = (t-i), li,li-offset,li+offset, if they are in they field
        #we need a flat list to flag the remaining slots, these are dfs branches, then traverse it,
        choice=[]
        self.dfs(0,choice,n)
        return self.solutions
        
    def dfs(self, line, choice, n):
        print(line,choice)
        #build branches
        flags=[False]*n
        for i in range(line):
            offset = line-i
            flags[choice[i]]=True
            self.mark(flags,n,choice[i]-offset)
            self.mark(flags,n,choice[i]+offset)
        #print("available:",flags)
        #choose
        if line==n-1:
            for i in range(n):           #build matrix return
                if not flags[i]:
                    choice.append(i)
                    self.solutions.append(self.buildMatrix(choice,n))
                    choice.pop()
                    #print("so:",self.solutions)
            return
        for i in range(n):
            if not flags[i]:
                choice.append(i)
                self.dfs(line+1, choice, n)
                choice.pop()

                
            
    def mark(self,flags,n,pos):
        if 0 <= pos <= n-1:
            flags[pos]=True
    def buildMatrix(self,choice,n):
        matrix = [["." for i in range(n)] for j in range(n)]
        for i in range(n):
            matrix[i][choice[i]]='Q'
            matrix[i]="".join(matrix[i])
        return matrix
  