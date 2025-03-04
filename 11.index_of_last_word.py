class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split()
        return len(words[-1])




test = Solution()
s = "Hello World"
s = "   fly me   to   the moon  "
print(test.lengthOfLastWord(s))