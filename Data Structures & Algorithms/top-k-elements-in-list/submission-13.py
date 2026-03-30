class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        return [j[0] for j in sorted(d.items(), reverse=True, key=lambda x:x[1])][:k]