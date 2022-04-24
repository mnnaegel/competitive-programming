class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setnums = set(nums)
        
        if not nums:
            return 0
        
        longest = 1
        while len(setnums) > 0:
            current = 1
            num = setnums.pop()
            start = num
            while num + 1 in setnums:
                num += 1
                current += 1
                longest = max(longest,current)
                setnums.remove(num)
            num = start
            while num - 1 in setnums:
                num -= 1
                current += 1
                longest = max(longest,current)
                setnums.remove(num)
                
        return longest
                