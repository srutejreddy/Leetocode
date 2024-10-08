class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        start, end = 0, 0 

        def LP(l,r):
            while l>=0 and r<N and s[l]==s[r]:
                l-=1
                r+=1
            return l+1, r-1

        for i in range(N):
            l, r = LP(i, i)
            if r-l+1 > end-start+1:
                start, end = l, r
            
            l, r = LP(i, i+1)
            if r-l+1 > end-start+1:
                start, end = l,r
                
        return s[start: end+1]