class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        snums = sorted(list(set(nums)))
        best = 1
        cur = 1
        for i in range(1,len(snums)):
            if snums[i]==snums[i-1]+1:
                cur+=1
            else:
                best=max(best,cur)
                cur=1
        return max(best,cur)
