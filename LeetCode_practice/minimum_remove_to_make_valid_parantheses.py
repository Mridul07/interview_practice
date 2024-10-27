class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        counter = 0
        for c in s:
            if c == '(':
                counter += 1
                res.append(c)
            elif c == ')' and counter > 0:
                counter -= 1
                res.append(c)
            elif c != ')':
                res.append(c)
        filtered_s = []
        for c in res[::-1]:
            if c == '(' and counter > 0:
                counter -= 1
            else:
                filtered_s.append(c)
        
        return ''.join(filtered_s[::-1])
