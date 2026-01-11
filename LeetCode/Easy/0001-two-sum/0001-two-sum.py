class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(0,len(nums)):
            if nums[i] in numsDict.keys():
                return [numsDict[nums[i]],i]
            else:
                numsDict[target-nums[i]] = i