class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        d_s={}
        d_t={}

        for i in range(len(s)):
            d_s[s[i]]=d_s.get(s[i],0)+1
            d_t[t[i]]=d_t.get(t[i],0)+1

        for x in d_s.keys():
            if x in d_s.keys() and x in d_t.keys():
                if d_s[x] == d_t[x]:
                    continue
                else:
                    return False
            else:
                return False
        return True
