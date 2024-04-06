class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        index = 0

        while (l <= r):
            index = (l + r) // 2
            if target == nums[index]:
                return index
            elif (target > nums[index]):
                l = index + 1
            else:
                r = index - 1

        return -1
