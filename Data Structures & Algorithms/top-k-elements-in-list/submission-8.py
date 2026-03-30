class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            d[nums[i]]=1+d.get(nums[i],0)
        
        return [x[0] for x in sorted(d.items(),key=lambda x:x[1],reverse=True)[:k]]