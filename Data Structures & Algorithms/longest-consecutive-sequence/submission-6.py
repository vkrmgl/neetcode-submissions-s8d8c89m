class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        best = 1
        cur = 1

        numset = list(set(nums))

        for i in range(len(numset)):
            if numset[i]-1 not in numset:
                counter = 1
                while numset[i]+counter in numset:
                    cur+=1
                    counter+=1
                best = max(best,cur)
                cur = 1
        
        return best