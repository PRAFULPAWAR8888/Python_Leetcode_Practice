class Solution:
    def twoSum(self, nums, target):

        n = len(nums)
        for i in range(n):
            complement = target - nums[i]

            for j in range(i+1,n):
                if nums[j] == complement:
                    return [i , j]

          

   

            
                


        





        

         
       


        