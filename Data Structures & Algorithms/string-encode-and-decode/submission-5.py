class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s = ''

        for w in strs:
            s+=str(len(w))+'#'+str(w)
        return s

    def decode(self, s: str) -> List[str]:

        i = 0

        ans = []

        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            i=j+int(s[i:j])
            ans.append(s[j+1:i+1])
            i+=1
        return ans

# 5#hello4#this