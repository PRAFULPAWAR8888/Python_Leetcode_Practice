class Solution:
    def countBits(self, n: int) -> List[int]:

        check = []
        count = []

        for i in range(n+1):
            binary = bin(i)[2:]
            check.append(binary)

            one_count = 0

            for bit in binary:
                if bit == "1":
                    one_count += 1
            count.append(one_count)
        
        return count

        
        