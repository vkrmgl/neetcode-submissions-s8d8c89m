class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for s in strs:
            w_map = [0]*26
            for c in s:
                w_map[ord(c)-ord('a')]+=1
            d[tuple(w_map)].append(s)
        
        return [x[1] for x in d.items()]