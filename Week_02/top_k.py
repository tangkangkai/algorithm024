import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        heap = []
        
        for i in counter:
            heappush(heap, (-counter[i], i))
            
        res = []
        
        for i in range(k):
            res.append(heappop(heap)[1])
            
        return res
        