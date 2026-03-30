class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        best = 0

        numset = set(nums)

        for i in range(len(nums)):

            if nums[i]-1 in numset:
                continue

            counter = 1
            
            while nums[i]+counter in numset:
                counter+=1
            
            best = max(best,counter)
        
        return best