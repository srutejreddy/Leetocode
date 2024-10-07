class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            d = point[0]**2+point[1]**2
            heapq.heappush(h, (-d,point))
            if len(h)>k:
                heapq.heappop(h)

        return [point for d,point in h]