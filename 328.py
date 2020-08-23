# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        evenhead=ListNode(0)
        odd=head
        even=evenhead
        while odd.next and odd.next.next :
            even.next=odd.next
            even=even.next
            odd.next=odd.next.next
            odd=odd.next
        if odd.next:
            even.next=odd.next
            even=even.next
            odd.next=evenhead.next
        else:
            odd.next=evenhead.next
        return head



New = Solution()
New.oddEvenList([1,2,3,4,5])