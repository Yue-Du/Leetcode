class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena=len(a)
        lenb=len(b)
        if lena>lenb:
            b=b.zfill(lena)
        else:
            a=a.zfill(lenb)
        b=b[::-1]
        a=a[::-1]
        add=""
        summ=0
        i=0
        while i < len(a):
            add=add + str((int(a[i])+int(b[i])+summ)%2)
            if int(a[i])+int(b[i])+summ>=2:
                summ=1
            else:
                summ=0
            i=i+1
        if summ==1:
            add=add+str(summ)
        return add[::-1]
new = Solution()
new.addBinary("1111","1111")

