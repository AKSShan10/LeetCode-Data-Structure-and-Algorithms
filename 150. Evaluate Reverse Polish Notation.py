class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []
        for i in tokens:
            if i == '+':
                sta.append(sta.pop()+sta.pop())
            elif i == '*':
                sta.append(sta.pop()*sta.pop())
            elif i == '-':
                b,a = sta.pop(),sta.pop()
                sta.append(a-b)
            elif i == '/':
                b,a = sta.pop(),sta.pop()
                sta.append(int(a/b))
            else:
                sta.append(int(i))
        print('stack',sta)
        return sta[0]