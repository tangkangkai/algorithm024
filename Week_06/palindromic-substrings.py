class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        ans = 0
        
        # res[i][i] is always true
        for i in range(len(s)):
            res[i][i] = 1
            ans += 1
        
        # now process 2
        for i in range(len(s) - 1):
            res[i][i + 1] = 1 if s[i] == s[i + 1] else 0
            ans += res[i][i + 1]
        
        # now process 3 and up
        for i in range(2, len(s)):
            for j in range(len(s) - i):
                res[j][j + i] = 1 if s[j] == s[j + i] and res[j + 1][j + i - 1] else 0
                ans += res[j][j + i]
                
        return ans