from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        number=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','C','IV','I']
        index=0
        res=''
        while index < len(number):
            while num<number[index]:
                index=index+1
            while num>=number[index]:
                res=res+roman[index]
                num=num-number[index]
            index = index + 1
        return res

New = Solution()
New.intToRoman(4)