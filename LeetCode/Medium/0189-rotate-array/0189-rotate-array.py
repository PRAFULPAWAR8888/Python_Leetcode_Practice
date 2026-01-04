class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        while k >=n:
            k -= n
        
        nums.reverse()

        nums[:k] = reversed(nums[:k])


        nums[k:] = reversed(nums[k:])
        """
        Do not return anything, modify nums in-place instead.
        """
