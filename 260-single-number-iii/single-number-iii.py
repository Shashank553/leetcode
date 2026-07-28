from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap=Counter(nums)
        ans=[]
        for x in hashmap:
            if hashmap[x]==1:
                ans.append(x)
        return ans