class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index_map = {v : i for i, v in enumerate(list1)}

        min_sum = float('inf')
        result = []

        for j, item in enumerate(list2):
            if item in index_map:
                total = index_map[item] + j
                if total < min_sum:
                    min_sum = total
                    result = [item]
                
                elif total == min_sum:
                    result.append(item)
        
        return result

        

        


        