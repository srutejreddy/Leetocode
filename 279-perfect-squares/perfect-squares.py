class Solution:
    def numSquares(self, n: int) -> int:
        if int(n**0.5) ** 2 == n:
            return 1

        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        queue = deque([(n, 0)]) 
        visited = set([n])

        while queue:
            value, steps = queue.popleft()

            for square in squares:
                next_value = value - square
                if next_value == 0:
                    return steps + 1
                if next_value < 0:
                    break
                if next_value not in visited:
                    visited.add(next_value)
                    queue.append((next_value, steps + 1))

        return n