class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for w in strs:
            letter = [0]*26
            for l in w:
                letter[ord('a')-ord(l)]+=1
            d[tuple(letter)].append(w)
        
        return list(d.values())
        