from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        result = sorted(freq, key=freq.get, reverse=True)

        return ''.join(c * freq[c] for c in result)