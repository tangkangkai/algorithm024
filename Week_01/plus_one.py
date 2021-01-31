class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + curr
            digits[i], curr = s % 10, 1 if s == 10 else 0
            
        if curr == 1:
            return [1] + digits
        
        return digits
            