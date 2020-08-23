class Solution:
    def isPalindrome(self, x: int) -> bool:
        f = list(str(x).split())
        l = len(f)
        if l % 2 == 0:
            t = l // 2
            l5 = f[:t]
            l2 = f[t:l]
            if l5 == l2.reverse():
                return True
            else:
                return False
        if l % 2 == 1:
            ll1 = f[:(l - 1) // 2]
            ll2 = f[(l + 1) // 2:l]
            if ll1 == ll2.reverse():
                return True
            else:
                return False

