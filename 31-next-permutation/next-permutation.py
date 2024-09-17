class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
         # 1 2 4 3 1 -> 1 2 4 3 1
        N = len(nums)
        idx = -1
        for i in range(N-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        if idx == -1:
            nums.sort()
            return

        for i in range(N-1,-1,-1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        left, right = idx+1, N-1
        while left<right:
            nums[left], nums[right] = nums[right],nums[left]
            left+=1
            right-=1