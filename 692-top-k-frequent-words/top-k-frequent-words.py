class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        c = [(-v,k) for k,v in c.items()]

        heapq.heapify(c)
        output = []

        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])    

        return output