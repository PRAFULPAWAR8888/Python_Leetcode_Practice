class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        

        curr = 1
        best = 1

        for i in range(len(nums)  - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
                best = max(best, curr)
            else:
                curr = 1
        
        return best
        