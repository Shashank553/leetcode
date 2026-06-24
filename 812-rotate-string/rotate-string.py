class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        '''return sorted(s)==sorted(goal)'''
        return len(s)==len(goal) and goal in (s+s)