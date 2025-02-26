class Solution:
    def isValid(self, s):
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            if char in brackets:
                top_element = stack.pop() if stack else "#"

                if brackets[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack                    


test = Solution()
print(test.isValid("()[]{}"))
print(test.isValid("()"))
print(test.isValid("()]"))