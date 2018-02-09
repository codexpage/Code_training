
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #if you use / instead of // you will get the float version of newton method.
        #in theory, t*t will infinitely approach x but always bigger than x, but in code
        #float will lose precison,and //make it lose some vale
        #so it could be smaller than sqrt(x)
        t=x
        while t*t>x:
            t=(t+x//t)//2
        return t
        
        #this method would cause timeout, too slow
        #at least use binary or quadary method
        #but newton is the best method!, and can solve float sqrt problem
        
        # if x==0:
        #     return 0
        # if x==1:
        #     return 1
        # for i in range(x//2+2):
        #     if i*i > x:
        #         return i-1
        #     if i*i == x:
        #         return i
        
        