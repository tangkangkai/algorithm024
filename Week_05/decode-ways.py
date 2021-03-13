class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        first = 1 if self.is_single_valid(s[0]) else 0
        
        if len(s) == 1 or not first:
            return first
        
        second = (first if self.is_single_valid(s[1]) else 0) + (1 if self.is_double_valid(s[:2]) else 0)
        
        if len(s) == 2 or not second:
            return second
        
        third = None
        
        for i in range(2, len(s)):
            if i > 2:
                first, second = second, third
            third = (second if self.is_single_valid(s[i]) else 0) + (first if self.is_double_valid(s[i - 1 : i + 1]) else 0)
            if not third:
                return 0
        
        return third
        
        
    def is_single_valid(self, s: str) -> bool:
        return 1 <= int(s) <= 9
    
    def is_double_valid(self, s: str) -> bool:
        return 10 <= int(s) <= 26
            
            
        
        
        
                