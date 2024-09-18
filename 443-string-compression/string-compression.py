class Solution:
    def compress(self, chars: List[str]) -> int:
        def addCountToChars(idx, count, chars):
            if count == 1:
                return idx
            elif count < 10:
                chars[idx] = str(count)
                idx+=1
            else:
                for s in str(count):
                    chars[idx] = s
                    idx+=1
            return idx

        N = len(chars)
        currChar = chars[0]
        count = 1
        idx = 0
        for i in range(1,N):
            if chars[i] == currChar:
                count+=1
            else:
                chars[idx] = currChar
                idx+=1
                idx = addCountToChars(idx, count, chars)
                currChar = chars[i]
                count = 1
        chars[idx] = currChar
        idx+=1
        idx = addCountToChars(idx,count,chars)
        return idx