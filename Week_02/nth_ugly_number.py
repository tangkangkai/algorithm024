import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 1:
            return n
        
        s = set()
        h = [1]
        while n > 0:
            val = heappop(h)
            
            if val in s:
                continue
            else:
                s.add(val)
            
            heappush(h, val * 2)
            heappush(h, val * 3)
            heappush(h, val * 5)
            n -= 1
            
        return val
        
        
        
        