class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i=0
        secret=list(secret)
        guess=list(guess)
        all_same=0
        sub_same=0
        while i <len(secret):
            if secret[i]==guess[i]:
                all_same +=1
                secret.pop(i)
                guess.pop(i)
            else:
                i=i+1
        secret.sort()
        guess.sort()
        while i <len(secret):
            if guess==[]:
                break
            elif secret[i] in guess:
                guess.remove(secret[i])
                sub_same +=1
            i=i+1
        return all_same,sub_same


New = Solution()
New.getHint("1807","7810")