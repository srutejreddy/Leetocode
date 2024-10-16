class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = {'a': a, 'b': b, 'c': c}

        while True:
            items = sorted(counts.items(), key=lambda x: -x[1])
            has_added = False
            for char, count in items:
                if count <= 0:
                    continue
                if len(result) >= 2 and result[-1] == result[-2] == char:
                    continue 

                result.append(char)
                counts[char] -= 1
                has_added = True
                break 

            if not has_added:
                break 

        return ''.join(result)