class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences={}
        for i in range(len(nums)):
            if nums[i] in occurences.values():
                return True
            occurences[i]=nums[i]
        return False