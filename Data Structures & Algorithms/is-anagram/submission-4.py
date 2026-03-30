class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        sdict, tdict = {},{}

        for x in range(len(s)):
            sdict[s[x]]=1+sdict.get(s[x],0)
            tdict[t[x]]=1+tdict.get(t[x],0)
        
        if sdict==tdict:
            return True
        
        return False
