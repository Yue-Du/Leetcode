from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol=['+','-','*','/']
        res=[]
        for item in tokens:
            if item not in symbol:
                res.append(item)
            else:
                left=res[-2]
                right=res[-1]
                res.pop()
                res.pop()
                if item == '+':
                    res.append(int(left)+int(right))
                if item == '-':
                    res.append(int(left)-int(right))
                if item == '*':
                    res.append(int(left)*int(right))
                if item == '/':
                    res.append(int(left) // int(right))
        return res[0]

New = Solution()
New.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])