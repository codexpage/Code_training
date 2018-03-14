class Solution:
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        return getlist(temp)

    
    
#using a stack to store the current element that can't find a bigger temp yet, which means the element is desending from bottom to top. 
def getlist(temp):
    s=[]
    res=[0 for x in temp]
    for i in range(len(temp)):
        
        while s:
            if temp[i] > temp[s[-1]]:
                res[s[-1]]=i-s[-1]
                s.pop()
            else:
                s.append(i)
                break
        if not s:
            s.append(i)
    return res

        
            
    
    
    
    
    
#TLE method


# def getlist(temp):
#     res=[]
#     for i in range(len(temp)):
#         for j in range(i,len(temp)):
#             if temp[j]>temp[i]:
#                 res.append(j-i)
#                 break
#             if j==len(temp)-1:
#                 res.append(0)
        
#     return res
