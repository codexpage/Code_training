#It's not easy 
#first we need a O(n^2) algo, not a naive(n^3) think about 2sum using hashing with O(n)
#this is n* 2sum, so we got O(n^2), for each number, check the rest to the end elements in the list of 2sum
#But the real problem is how to make the solution unique?
#First I try to convert it into set(), but TLE take too much time
#Then I think about sort and check duplicated element. also TLE
#Then I figure: we can sort at fisrt take O(nlogn), and the result must be sorted without adding complexity
#Second is how to check duplication without adding complexity:
#of course 2sum result must first be unique
#do it in the loop, when the list is sorted like -4 -1 -1 0 1 2
#the second -1's subresult must be contained in the first -1's subresult, this cause the duplication.
#if we just care about the first -1 in a list like 0 -1 -1 -1 2 3, skip the rest of -1 the result will be unique
#this save a lot of time

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplet=[]
        nums.sort()
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            pairs = self.twoSum(nums[i+1:],-nums[i])
            if pairs!=[]:
                triplet.extend([[nums[i]]+pair for pair in pairs])
        # sortl = [tuple(sorted(li)) for li in triplet]
        # triplet = list(set(sortl))
        # triplet = [list(li) for li in triplet]
        
        # triplet = list(set([tuple(li) for li in triplet]))
        # triplet = [list(li) for li in triplet]
        
        return triplet
        
    def twoSum(self, nums, sumv):
        h={}
        pairs=[]
        for num in nums:
            if not num in h:
                h[sumv-num]=1
            else:
                if not [sumv-num,num] in pairs:
                    pairs.append([sumv-num,num])
        return pairs
        
        
            
    