class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        
        last = {int(d): i for i, d in enumerate(num_list)}
        
        for i in range(n):
            current_digit = int(num_list[i])
            for d in range(9, current_digit, -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]

                    return int(''.join(num_list))
            
        return num