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


# more pythonic solution:

# class Solution:
#     def plusOne(self, digits):
#         return list(map(int, str(int("".join(map(str, digits))) + 1)))


test = Solution()
digits = [1,2,3]
print(test.plusOne(digits))