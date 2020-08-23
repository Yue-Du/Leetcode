# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or head.next == None:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        half2 = slow.next
        slow.next = None

        pre = half2
        cur = pre.next
        pre.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            second = pre.next
        return True


New = Solution()
New.isPalindrome([1,2,2,1])