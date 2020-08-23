class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        length1,length2 = 0,0
        current1,current2 = l1,l2
        while current1:
            length1 +=1
            current1 = current1.next
        while current2:
            length2 +=1
            current2 = current2.next
        if length1>=length2:
            l3=l1
        else:
            l3=l2
        current=l3
        index=0
        while l1 and l2:
            if l1.val+l2.val<10:
                current.val=l1.val+l2.val+index
                index=0
            else:
                current.val=l1.val+l2.val+index-10
                index=1
            l1=l1.next
            l2=l2.next
            current=current.next
        while l1 and not l2:
            if l1.val+index<10:
                current.val=l1.val+index
                index=0
            else:
                current.val=l1.val+index-10
                index=1
            current=current.next
            l1=l1.next
        while l2 and not l1:
            if l2.val+index<10:
                current.val=l2.val+index
                index=0
            else:
                current.val=l2.val+index-10
                index=1
            current=current.next
            l2=l2.next
        if index==1:
            current=ListNode(index)
        return l3


New = Solution()
New.addTwoNumbers([2,4,3],[5,6,4])