class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        window = N-k
        currSum = sum(cardPoints[:window])
        totalSum, minSum = sum(cardPoints), currSum
        
        l = 0
        for r in range(window,N):
            currSum+=cardPoints[r]-cardPoints[l]
            minSum = min(currSum, minSum)
            l+=1

        return totalSum-minSum