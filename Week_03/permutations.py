class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        self.backtrack(nums, res, curr, set())
        
        return res
        
    def backtrack(self, nums, res, curr, used):
        if len(curr) == len(nums):
            res.append(curr[::])
            return
        
        for num in nums:
            if num not in used:
                used.add(num)
                curr.append(num)
                self.backtrack(nums, res, curr, used)
                used.remove(num)
                curr.pop()
        