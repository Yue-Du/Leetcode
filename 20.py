class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        right=[')',']','}']
        stack=[]
        for item in s:
            if item not in right:
                stack.append(item)
            else:
                if item==')':
                    if stack[-1]!='(':
                        return False
                    else:
                        stack.pop()
                if item==']':
                    if stack[-1]!='[':
                        return False
                    else:
                        stack.pop()
                if item=='}':
                    if stack[-1]!='{':
                        return False
                    else:
                        stack.pop()
        return True


New = Solution()
New.isValid("()[]{}")