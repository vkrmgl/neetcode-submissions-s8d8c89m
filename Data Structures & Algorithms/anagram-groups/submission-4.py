class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        for w in strs:
            word = [0]*26
            for i in range(len(w)):
                word[ord('a')-ord(w[i])]+=1
            d[tuple(word)].append(w)
        
        return list(d.values())