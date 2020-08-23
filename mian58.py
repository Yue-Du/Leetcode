class Solution:
    def reverseWords(self, s: str) -> str:
        if not str:
            return ""

        word=[]
        new_s = s.strip()
        begin = 0
        for i in range(len(new_s)):
            if new_s[begin] == " ":
                begin+=1
                continue
            if new_s[i] == " ":
                word.append(new_s[begin:i])
                begin=i+1
        word.append(new_s[begin:i+1])
        word = word[::-1]
        return " ". join(word)


New = Solution()
New.reverseWords("")