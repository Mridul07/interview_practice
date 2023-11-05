class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        res1 = "".join(re.split("[^a-zA-Z0-9]*", s))
        res1 = res1.lower()

        return res1 == res1[::-1]