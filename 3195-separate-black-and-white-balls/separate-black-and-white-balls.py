class Solution:
    def minimumSteps(self, s: str) -> int:
        totalSwaps = 0
        whiteCount = 0 
        for char in reversed(s):
            if char == '0':
                whiteCount += 1
            else:
                totalSwaps += whiteCount
        return totalSwaps