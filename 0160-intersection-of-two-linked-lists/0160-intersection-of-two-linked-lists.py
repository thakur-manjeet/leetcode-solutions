# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first=headA
        second=headB

        while first!=second:
            if first is None:
                first=headB
            else:
                first=first.next
            
            if second is None:
                second=headA
            else:
                second=second.next     
        return first        