class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            if nums[i] in numsDict:
                print("yes nums[i] in numsdicst")
                return [numsDict[nums[i]], i]
            numsDict[target - nums[i]] = i
