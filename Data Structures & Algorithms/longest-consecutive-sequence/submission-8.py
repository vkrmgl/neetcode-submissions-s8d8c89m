class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        snums = set(nums)

        best = 0

        for i in range(len(nums)):
            if nums[i]-1 not in snums:
                length = 1
                while nums[i]+length in snums:
                    length+=1
                best = max(best, length)
        return best
