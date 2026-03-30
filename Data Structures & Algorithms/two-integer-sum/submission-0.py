class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in d:
                return [min(i,d.get(diff)),max(i,d.get(diff))]
            d[n]=i