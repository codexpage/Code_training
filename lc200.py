#simple dfs
#be careful x is bound by height, y is bounded by witdh!
#special case: [] should return 0

class Solution:
    flags = None
    height = None
    width = None
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid==[]:
            return 0
        self.height = len(grid)
        self.width = len(grid[0])
        count = 0
        self.flags = [[(False if grid[i][j]=="1" else True) for j in range(self.width)] for i in range(self.height)]
#         self.pm(self.flags) 
        for i in range(self.height):
            for j in range(self.width):
                if not self.flags[i][j]:
                    self.dfs(i,j)
                    count+=1
#                     print("plus 1")
        return count
        #for each unvisted point, dfs it, count++
    
    def dfs(self,x,y):
        #generate braches, no branch: return
        #choose one, mark it
#         print(x," ",y)
        for di in [[-1,0],[1,0],[0,-1],[0,1]]:
            dx = x + di[0]
            dy = y + di[1]
            if self.unvisited(dx,dy):
                self.flags[dx][dy]=True #mark
#                 print("dx:",dx," ","dy:",dy)
#                 self.pm(self.flags)
                self.dfs(dx,dy) #search
        #after traverse all braches
        return
            
    #return true if not visited
    def unvisited(self, x, y):
        width=self.width
        height=self.height
        if 0 <= x < height and 0 <= y < width and not self.flags[x][y]:
            return True
        else:
            return False
    def pm(self, matrix):
#         print(" ")
        for line in matrix:
                print("".join([('0' if char else '1') for char in line]))    
        
        
    