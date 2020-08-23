class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        length = len(searchWord)
        sent_list = sentence.split()
        i=0
        while i < len(sent_list):
            if len(sent_list[i]) < length:
                i+=1
            elif sent_list[i][:length]  == searchWord:
                return i+1
            else:
                i+=1
        return -1


New = Solution()
New.isPrefixOfWord("i love eating burger","burg")