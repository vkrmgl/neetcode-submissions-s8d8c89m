class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        c_map = [0]*26

        for i in range(len(s)):
            c_map[ord(s[i])-ord('a')]+=1
            c_map[ord(t[i])-ord('a')]-=1
        
        return c_map == [0]*26