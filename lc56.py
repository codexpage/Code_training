# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """ 
        intervals.sort(key= lambda x: x.start)
        res =[]
        for inte in intervals:
            if res==[] or res[-1].end<inte.start:
                res.append(inte)
            else:
                res[-1].end = max(res[-1].end,inte.end)
        return res
                