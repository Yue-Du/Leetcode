#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p=head
        q=head.next
        while q is not None:
            p.next=q.next
            q.next=p
            p=p.next
            if p is not None:
                q=p.next
            else:
                break
        return head


New = Solution()
New.swapPairs([1,2,3,4])