class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        searched = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in searched:
                return [searched[diff], i]
            searched[nums[i]]=i
        return []