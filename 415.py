class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        number1=0
        number2=0
        i=0
        j=0
        len1=len(num1)-1
        len2=len(num2)-1
        while i < len(num1):
            number1 =number1+int(num1[i])*10**len1
            i=i+1
            len1=len1-1
        while j < len(num2):
            number2 = number2+int(num2[j])*10**len2
            j=j+1
            len2=len2-1
        output = str(number1+number2)
        return output


New = Solution()
New.addStrings("98","9")