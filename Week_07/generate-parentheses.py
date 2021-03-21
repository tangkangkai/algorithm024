class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        
        self.helper(curr, 0, 0, res, n)
        
        return res
        
    def helper(self, curr, left, right, res, n):
        if len(curr) == 2 * n:
            res.append("".join(curr))
            return
        
        if left < n:
            curr.append("(")
            self.helper(curr, left + 1, right, res, n)
            curr.pop()
        
        if right < left:
            curr.append(")")
            self.helper(curr, left, right + 1, res, n)
            curr.pop()
        