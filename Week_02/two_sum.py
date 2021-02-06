class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}
        
        for i in range(len(nums)):
            if target - nums[i] in val_to_index:
                return [val_to_index[target - nums[i]], i]
            else:
                val_to_index[nums[i]] = i
        
        return [] 