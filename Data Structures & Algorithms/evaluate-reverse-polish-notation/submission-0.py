class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for i in range(len(tokens)):
            if tokens[i]=='+':
                stk.append(stk.pop()+stk.pop())
            elif tokens[i]=='-':
                b,a=stk.pop(), stk.pop()
                stk.append(a-b)
            elif tokens[i]=='/':
                b,a=stk.pop(), stk.pop()
                stk.append(int(a/b))
            elif tokens[i]=='*':
                stk.append(stk.pop()*stk.pop())
            else:
                stk.append(int(tokens[i]))

        return stk[0]

            
            