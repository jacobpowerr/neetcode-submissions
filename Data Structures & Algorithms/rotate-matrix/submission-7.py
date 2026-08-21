class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            t, b = l, r

            for i in range(r - l):
                
                topLeft = matrix[t + i][l]

                matrix[t + i][l] = matrix[b][l + i]

                matrix[b][l + i] = matrix[b - i][r]

                matrix[b - i][r] = matrix[t][r - i]

                matrix[t][r - i] = topLeft
            
            l += 1
            r -= 1