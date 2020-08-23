class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s=list(s)
        step=2*numRows-2
        res=[[]for i in range(numRows)]
        k=0
        while k*step < len(s):
            res[0].append(s[0+k*step])
            k=k+1
        i=1
        while i < numRows-1:
            row_start = i
            res[i].append(s[row_start])
            while row_start+(step-2*i) < len(s):
                row_start=row_start+(step-2*i)
                res[i].append(s[row_start])
                if row_start+(2*i) < len(s):
                    row_start=row_start+(2*i)
                    res[i].append(s[row_start])
                else:
                    break
            i=i+1
        res[numRows-1].append(s[numRows-1])
        h=1
        row_n=numRows-1
        while row_n+step < len(s):
            row_n=row_n+h*step
            res[numRows-1].append(s[row_n])

        output = []
        for row in range(numRows):
            for t in range(len(res[row])):
                output.append(res[row][t])
        return output



New = Solution()
New.convert("PAYPALISHIRING",4)