class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxLeft = [-1]
        maxRight = [-1]
        
        if not height:
            return 0
        
        cmaxleft = height[0]
        for i,h in enumerate(height):
            cmaxleft = max(cmaxleft, h)
            maxLeft.append(cmaxleft)
        
        cmaxright = height[-1]
        for h in height[::-1]:
            cmaxright = max(cmaxright, h)
            maxRight.append(cmaxright)
        maxRight = maxRight[::-1]
        
        volume = 0
        for i in range(len(height)):
            containerHeight = min(maxLeft[i],maxRight[i])
            adjustedHeight = containerHeight - height[i]
            if adjustedHeight > 0:
                volume += adjustedHeight
        return volume
            
            