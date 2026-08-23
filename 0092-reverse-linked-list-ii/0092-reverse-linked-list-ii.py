# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        curr=head
        left_prev=dummy

        for i in range(left-1):
            left_prev=left_prev.next
            curr=curr.next

        subList_head=curr

        prev=None

        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr

            curr=nxt

        left_prev.next=prev
        subList_head.next=curr

        return dummy.next     