class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        res = ""
        maxLen = 0

        for i in range(N):
            l, r = i, i
            while l>=0 and r<N and s[l]==s[r]:
                currLen = r-l+1
                if currLen>maxLen:
                    res = s[l:r+1]
                    maxLen = currLen
                l-=1
                r+=1
            
            l, r = i, i+1
            while l>=0 and r<N and s[l]==s[r]:
                currLen = r-l+1
                if currLen>maxLen:
                    res = s[l:r+1]
                    maxLen = currLen
                l-=1
                r+=1

        return res