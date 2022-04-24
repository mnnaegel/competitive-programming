class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height)- 1
        
        maxvolume = min(height[left],height[right])*(right-left)
        
        while left < right:
            maxvolume = max(maxvolume,(right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        
        return maxvolume