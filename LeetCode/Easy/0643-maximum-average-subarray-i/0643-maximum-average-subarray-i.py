class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Step 1 : initial window sum

        window_sum = sum(nums[:k])
        max_sum = window_sum

        # step 2 : slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]  # add next elements
            window_sum -= nums[i - k] #remove left elements

            max_sum = max(max_sum, window_sum)

        #Step 3: return average

        return max_sum/k        