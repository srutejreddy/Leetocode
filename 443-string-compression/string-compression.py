class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        N = len(chars)

        while fast < N:
            currChar = chars[fast]
            count = 0

            while fast<N and chars[fast] == currChar:
                fast+=1
                count+=1
            
            chars[slow] = currChar
            slow+=1
            if count>1:
                for s in str(count):
                    chars[slow] = s
                    slow+=1
        return slow