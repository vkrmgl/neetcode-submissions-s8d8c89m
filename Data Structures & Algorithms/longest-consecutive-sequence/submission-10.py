class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0

        nset = set(nums)

        glong = 0

        for n in nset:
            curr = n
            longest=1
            while curr+1 in nset:
                curr+=1
                longest+=1
            glong=max(longest,glong)

        return glong