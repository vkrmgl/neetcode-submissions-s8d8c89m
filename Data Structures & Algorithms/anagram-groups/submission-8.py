class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = defaultdict(list)

        for i in range(len(strs)):
            sortedw = ''.join(sorted(strs[i]))
            grams[sortedw].append(strs[i])
        
        return list(grams.values())