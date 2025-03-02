class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
test = Solution()
print(test.strStr(haystack, needle))