class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        dp = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

        def backtrack(start):
            if start == n:
                result.append(path.copy())
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result