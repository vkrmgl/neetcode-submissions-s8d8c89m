class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()

        for i in range(len(nums)):
            if nums[i] in checked:
                return True
            checked.add(nums[i])
        return False