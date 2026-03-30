class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = defaultdict(list)

        for i in range(len(strs)):
            word = [0]*26
            for c in strs[i]:
                word[ord(c)-ord('a')]+=1
            grams[tuple(word)].append(strs[i])

        return list(grams.values())