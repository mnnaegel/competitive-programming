class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freqcounter = defaultdict(int)
        
        for num in nums:
            freqcounter[num] += 1
        
        freqcounter = sorted(freqcounter, key=freqcounter.get, reverse=True)
        
        return freqcounter[:k]