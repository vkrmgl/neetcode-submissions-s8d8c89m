class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = sorted(list(set(nums)))
        nums[:len(x)]=x
        return len(x)