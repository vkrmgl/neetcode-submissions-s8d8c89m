class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        snums = list(set(nums))

        best = 0

        for i in range(len(snums)):
            if snums[i]-1 not in snums:
                length = 1
                while snums[i]+length in snums:
                    length+=1
                best = max(best, length)
        return best
