
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=previous=ListNode(0)
        if not (l1 or l2):
            return None
        while l1 and l2:
            if l1.val<=l2.val:
                previous.next=l1
                l1=l1.next
            else:
                previous.next=l2
                l2=l2.next
            previous=previous.next
        if l1:
            previous.next=l1
        else:
            previous.next=l2
        return head.next