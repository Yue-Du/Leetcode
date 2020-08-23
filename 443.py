from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        pre=0
        cur=1
        while cur <= len(chars):
            if chars[pre]==chars[cur] and cur < len(chars):
                count=count+1
                cur+=1
            else:
                if count==1:
                    pre+=1
                    cur+=1
                else:
                    k=1
                    while k <count:
                        chars.pop(1+pre)
                        k+=1
                    str_count=str(count)
                    length=len(str_count)
                    for i in range(length):
                        chars.insert(pre+i+1, str_count[i])
                    pre=pre+length+1
                    cur=pre+1
                    count=1
        return len(chars)

        '''length=len(chars)
        if length<2:return length
        l,r,count=0,1,1
        while r<=length:
            if r==length or chars[l]!=chars[r]:
                if count>1:
                    for i in str(count):
                        l+=1
                        chars[l]=i
                l+=1
                if r<length:chars[l]=chars[r]
                count=1
            else:count+=1
            r+=1
        return l'''


New = Solution()
New.compress(["a","a","b","b","c","c","c"])