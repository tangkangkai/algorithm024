class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        self.backtrack(nums, res, curr, Counter(nums))
        return res
        
    def backtrack(self, nums, res, curr, counter):
        if len(curr) == len(nums):
            res.append(curr[::])
            return
            
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                self.backtrack(nums, res, curr, counter)
                counter[num] += 1
                curr.pop()
        
                
                
                
            
                
                