class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        x_str = str(x)

        return x_str == x_str[::-1]

        
is_p = Solution()
print(is_p.isPalindrome(121))
print(is_p.isPalindrome(122))
