class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True

test = Solution()
print(test.isHappy(19))
print(test.isHappy(2))