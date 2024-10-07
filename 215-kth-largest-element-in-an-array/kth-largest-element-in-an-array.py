class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)

        while len(heap)>k:
            heapq.heappop(heap)
        res = heapq.heappop(heap)
        
        return res