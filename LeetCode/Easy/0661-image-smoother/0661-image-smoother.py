class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                
                total = 0
                count = 0
                
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        
                        neighbor_row = i + dx
                        neighbor_col = j + dy
                        
                        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                            total += img[neighbor_row][neighbor_col]
                            count += 1
                
                result[i][j] = total // count
        
        return result