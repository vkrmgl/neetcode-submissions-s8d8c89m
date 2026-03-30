class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        closeToOpen = {')':'(',']':'[','}':'{'}

        for i in range(len(s)):
            
            if st and s[i] in closeToOpen:
                if st[-1]==closeToOpen[s[i]]:
                    st.pop()
                else:
                    return False
            else:
                st.append(s[i])

        return True if not st else False
