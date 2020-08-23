# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text_list = text.split()
#         text_list.sort(key = lambda i: len(i))
#         for word in text_list:
#             word= word[0].upper() + word[1:]
#         return " ".join(text_list)
#
# New = Solution()
# New.arrangeWords("Leetcode is cool")