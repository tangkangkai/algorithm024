class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        str_list = s.strip().split(" ")
        
        res = []
        for s in str_list[::-1]:
            if s:
                res.append(s)
        
        return " ".join(res)