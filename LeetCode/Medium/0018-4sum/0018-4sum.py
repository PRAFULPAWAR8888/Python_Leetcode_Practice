class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):

                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        result.add(quad)
                    
                    seen.add(nums[k])
        return [list(t) for t in result]
                    

            


        