class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for w in strs:
            s+=str(len(w))+'#'+w
        return s

    def decode(self, s: str) -> List[str]:

        strs = []

        i = 0

        while i<len(s):
            j=i
            while s[i]!='#':
                i+=1
            wlen = int(s[j:i])
            j=i+1
            i=j+wlen
            strs.append(str(s[j:i]))

        return strs


