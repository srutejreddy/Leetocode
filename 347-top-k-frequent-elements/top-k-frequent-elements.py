class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = [(-v,k) for k,v in c.items()]
        heapq.heapify(c)

        res =[]
        for i in range(k):
            item = heapq.heappop(c)
            res.append(item[1])

        return res