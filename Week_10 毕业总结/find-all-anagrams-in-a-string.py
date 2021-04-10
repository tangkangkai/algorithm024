class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(p) > len(s):
            return []
        
        res = []
        
        counter_p = collections.Counter(p)
        counter_s = collections.Counter(s[0:len(p)])
        
        if counter_s == counter_p:
            res.append(0)
            
        for i in range(len(p), len(s)):
            if s[i] not in counter_s:
                counter_s[s[i]] = 1
            else:
                counter_s[s[i]] += 1
            
            counter_s[s[i - len(p)]] -= 1
            if not counter_s[s[i - len(p)]]:
                del counter_s[s[i - len(p)]]
        
            
            if counter_s == counter_p:
                res.append(i - len(p) + 1)
        return res