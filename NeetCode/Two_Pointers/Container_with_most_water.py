class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            tank_height = height[left] if height[left] < height[right] else height[right]
            width = right - left
            area = tank_height * width
            print(area)
            print(max_area)
            max_area = area if area > max_area else max_area
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        
        return max_area

