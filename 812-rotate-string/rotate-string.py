class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return sorted(s)==sorted(goal)