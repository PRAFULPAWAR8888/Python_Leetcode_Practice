class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        idx = nums.index(mx)

        for num in nums:
            if num == mx:
                continue
            
            if mx < 2 * num:
                return -1
        
        else:
            return idx
        