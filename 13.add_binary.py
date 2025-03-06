class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


test = Solution()
print(test.addBinary("11", "1"))
print(test.addBinary("1010", "1011"))