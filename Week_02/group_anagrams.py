import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            counter = self.get_count_arr(s)
            if counter in res:
                res[counter].append(s)
            else:
                res[counter] = [s]
        
        return res.values()
    
    def get_count_arr(self, s):
        res = [0] *26
        for ch in s:
            index = ord(ch) - ord('a')
            res[index] += 1
        return tuple(res)