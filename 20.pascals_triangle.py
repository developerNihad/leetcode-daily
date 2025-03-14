class Solution:
    def generate(self, numRows):
        triangle = []
        
        for row_num in range(numRows):

            row = [1] * (row_num + 1)

            for i in range(1, row_num):
                row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]

            triangle.append(row)
        
        return triangle

test = Solution()
print(test.generate(5)) 