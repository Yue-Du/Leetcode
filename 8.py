class Solution:
    def myAtoi(self, str: str) -> int:
        i=0
        all_type=[' ','0',"1","2","3","4","5",'6','7','8','9','+','-']
        num=['0',"1","2","3","4","5",'6','7','8','9']
        res=""
        sgn="+"
        if str=="":
            return 0
        if str[0] not in all_type:
            return 0
        while i< len(str) and str[i] ==" ":
                i=i+1
        if i>=len(str):
            return 0
        while i < len(str):
            if str[i]=="+" or str[i]=="-":
                sgn=str[i]
                i=i+1
            if i>=len(str) or str[i] not in num:
                return 0
            else:
                while i < len(str):
                    if str[i] in num:
                        res=res+str[i]
                        i=i+1
                    else:
                        break
                if int(sgn+res)<pow(-2,31):
                    return pow(-2,31)
                elif int(sgn+res)>pow(2,31)-1:
                    return pow(2,31)-1
                else:
                    return int(sgn+res)



New = Solution()
New.myAtoi("4193 with words")