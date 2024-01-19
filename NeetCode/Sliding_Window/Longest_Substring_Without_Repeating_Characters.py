class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        maxL = 0
        currSet = set()

        for r in range(len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxL = max(maxL, r - l + 1)

        return maxL