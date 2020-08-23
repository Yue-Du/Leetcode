from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=['z','x','c','v','b','n','m']
        row2=['a','s','d','f','g','h','j','k','l']
        row3=['q','w','e','r','t','y','u','i','o','p']
        res=[]
        for word in words:
            low_word=word.lower()
            if low_word[0] in row1:
                row=row1
            elif low_word[0] in row2:
                row=row2
            else:
                row=row3
            i=1
            while i <len(low_word):
                if low_word[i] in row:
                    i=i+1
                else:
                    break
            if i ==len(low_word):
                res.append(word)
        return res


New = Solution()
New.findWords(["qwee"])