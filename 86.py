#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp = ListNode(None)
        last = temp
        pre = ListNode(None)
        pre.next = head
        cur = pre
        while cur.next:
            if cur.next.val < x:
                cur = cur.next
            else:
                last.next = cur.next
                last = last.next
                cur.next = cur.next.next
        cur.next = temp.next
        return pre.next


New = Solution()
New.partition([1,4,3,2,5,2],3)
