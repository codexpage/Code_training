import math

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if answers==[]:
            return 0
        count={}
        for ans in answers:
            if ans in count:
                count[ans]+=1
            else:
                count[ans]=1
        #count 
        
        total = 0
        for key in count:
            num = count[key]
            groups = math.ceil(num/(key+1))
            rab_num = groups*(key+1)
            total += rab_num
        return total