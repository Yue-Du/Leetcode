class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        while headB:
            while headA:
                if headA != headB:
                    headA=headA.next
                else:
                    return headA.val
            headB=headB.next
        return None




New = Solution()
New.getIntersectionNode([4,1,8,4,5],[5,0,1,8,4,5])