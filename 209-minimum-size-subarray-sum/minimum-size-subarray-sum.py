class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        minLen = float('inf')
        left = 0
        currentSum = 0

        for right in range(N):
            currentSum+=nums[right]
            while currentSum >= target:
                minLen = min(minLen, right-left+1)
                currentSum-=nums[left]
                left+=1

        return minLen if minLen != float('inf') else 0