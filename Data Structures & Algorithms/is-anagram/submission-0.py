class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        ls=[]
        lt=[]
        
        for i in range(len(s)):
            ls.append(s[i])
            lt.append(t[i])

        if sorted(ls) == sorted(lt):
            return True
        
        return False