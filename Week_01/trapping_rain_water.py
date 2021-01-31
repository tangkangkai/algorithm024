class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        
        stack = []
        result = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                prev_i = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1
                height_diff = min(height[i], height[stack[-1]]) - height[prev_i]
                result += distance * height_diff
                
            stack.append(i)
        
        return result
            
                
            
        