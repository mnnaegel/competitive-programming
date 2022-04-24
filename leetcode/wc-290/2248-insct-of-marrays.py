class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        inall = []
        if not nums:
            return []
        for num in nums[0]:
            flag = True
            for k in range(len(nums)):
                if 0 == k:
                    continue
                if num not in nums[k]:
                    flag = False
            if flag:
                inall.append(num)
        inall.sort()
        return inall
        