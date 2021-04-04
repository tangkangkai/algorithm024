class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        
        letter_dict = collections.defaultdict()
        values_set = set()
        
        for i in range(len(s)):
            ch = s[i]
            
            if ch in letter_dict:
                if t[i] != letter_dict[ch]:
                    return False
                else:
                    continue
            else:
                if t[i] in values_set:
                    return False
                letter_dict[ch] = t[i]
                values_set.add(t[i])
        
        return True