class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}

        for i in range(len(nums)):
            val = target-nums[i]

            if val in arr:
                return [arr[val],i]

            arr[nums[i]]=i