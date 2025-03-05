class Solution:
    def plusOne(self, digits):
        s = ""
        for i in digits:
            s += str(i)

        n = int(s) + 1

        l = []

        for i in str(n):
            l.append(int(i))
        
        return l


test = Solution()
digits = [1,2,3]
print(test.plusOne(digits))