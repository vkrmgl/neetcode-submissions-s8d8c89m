class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = [0]*26
        two = [0]*26
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            one[ord('a')-ord(s[i])]+=1
            two[ord('a')-ord(t[i])]+=1

        if one==two:
            return True

        else: return False