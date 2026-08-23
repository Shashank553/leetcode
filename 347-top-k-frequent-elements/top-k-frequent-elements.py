class Solution(object):
    def topKFrequent(self, nums, k):
        
        freq = {}   # Create dictionary

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort numbers based on frequency
        result = sorted(freq, key=freq.get, reverse=True)

        return result[:k]