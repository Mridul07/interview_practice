class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        leftPointer, rightPointer = 0, len(numbers) - 1

        while (numbers[leftPointer] + numbers[rightPointer]) != target:
            if (numbers[leftPointer] + numbers[rightPointer]) > target:
                rightPointer -= 1
            elif (numbers[leftPointer] + numbers[rightPointer]) < target:
                leftPointer += 1
        
        return leftPointer + 1, rightPointer + 1