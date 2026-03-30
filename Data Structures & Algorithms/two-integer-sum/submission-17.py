class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={}

        for i, n in enumerate(nums):
            d[n]=i
        
        for i, n in enumerate(nums):
            diff = target-n

            if diff in d and i!=d[diff]:
                return [i, d[diff]]

        return []