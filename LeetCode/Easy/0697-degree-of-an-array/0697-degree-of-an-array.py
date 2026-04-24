class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        count = {} #frequency
        first = {} #first index
        last = {} #last index

        for i,n in enumerate(nums):
            if n not in count:
                count[n] = 0
                first[n] = i    # save first time seen
            
            count[n] += 1        
            last[n] = i          # keep updating last time seen
        
        degree = max(count.values()) # step 2
    
        result = len(nums)
        for n in count:
            if count[n] == degree:         # step 3 = only elements with highest degree
               length = last[n] - first[n] + 1 # step 4
               result = min(result, length)   #step 5
        return result
        