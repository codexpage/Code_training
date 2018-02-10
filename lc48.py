#we need to rotate in place, so we need to find a pattern to exchange the element in loop
#divide the square in the four sub-square, but we shuoln't count both edge, only one edge is counted,
#or the edge will be rotate twice.
#so x in math.ceil(n/2), y in range(math.floor(n/2)), this will exclude the center, center do not move

#we only iterate in the left-top one, and then
#for each element in the sub-square we shift it in a cirle with 3 other corresponding elements
# for (1,0)-> (0,2),(2,3),(3,1)  (x,y) ->(y,len-1-x),(len-1-x,len-1-y),(len-1-y,x)
# corner: (0,0)->(0,3)(3,3)(3,0), for 3-square center:(1,1)->(1,1)(1,1)(1,1) works
# to shift four elements is easy l.insert(l[-1],0) l.pop()


#be careful about edge cases
import math
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=n-1 # the max index
        for i in range(math.ceil(n/2)):
            for j in range(math.floor(n/2)):
                four_list=[]
                four_list.extend([matrix[i][j],matrix[j][m-i],matrix[m-i][m-j],matrix[m-j][i]])
                print(four_list)
                four_list.insert(0,four_list[-1])
                four_list.pop() #right shift(rotate)
                print("shifted:",four_list)
                matrix[i][j],matrix[j][m-i],matrix[m-i][m-j],matrix[m-j][i] = four_list #also work for center
        return
        