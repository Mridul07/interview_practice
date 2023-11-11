class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for index, element in enumerate(nums):
            if index > 0 and nums[index - 1] == element:
                continue
            l, r = index + 1, len(nums) - 1

            while l<r:
                three_sum = element + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else: 
                    res.append([element, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                
        return res
