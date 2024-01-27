class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapper = {
            ')': '(', 
            '}': '{',
            ']': '['
            }
        for c in s:
            if c in mapper:
                if stack and stack[-1] == mapper[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False