from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashtable = {'5':0,'10':0,'20':0}

        i = 0
        while i < len(bills):
            if bills[i] == 5:
                hashtable['5'] += 1
            if bills[i] == 10 and hashtable['5'] == 0:
                return False
            elif bills[i] == 10:
                hashtable['10'] += 1
                hashtable['5'] -= 1
            if (bills[i] == 20 and hashtable['10'] < 1 and hashtable['5'] <3) or (bills[i] == 20 and hashtable['10'] > 0 and hashtable['5'] < 1):
                return False
            elif bills[i] == 20 and hashtable['10'] > 0:
                hashtable['20'] += 1
                hashtable['10'] -= 1
                hashtable['5'] -= 1
            elif bills[i] == 20:
                hashtable['20'] += 1
                hashtable['5'] -=3
            i += 1
        return True


New = Solution()
New.lemonadeChange([5,5,5,10,20])