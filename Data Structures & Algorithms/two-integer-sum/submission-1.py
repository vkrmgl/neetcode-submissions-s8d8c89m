class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in d:
                return [d.get(diff), i]
            d[nums[i]]=i
        
        # 0 -> 4
        # 0: diff = 4, if diff in d: No, d[4]=0
        # 1: diff = 3, if diff in d: Yes, return [d.get]