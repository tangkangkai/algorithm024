class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return
        
        nums_copy = nums.copy()
        
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = nums_copy[i]