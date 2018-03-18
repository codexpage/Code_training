class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1={}
        count2={}
        for i in nums1:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        for i in nums2:
            if i not in count2:
                count2[i]=1
            else:
                count2[i]+=1
        for d in count1:
            if d not in count2:
                count1[d]=0
            else:
                count1[d]=min(count1[d],count2[d])
        res=[]
        for i in count1:
            res.extend([i]*count1[i])
        return res
          