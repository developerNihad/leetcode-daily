import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return clean_str == clean_str[::-1]


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
print(test.isPalindrome("race a car"))
print(test.isPalindrome(" "))