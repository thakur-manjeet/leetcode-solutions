# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head

        while count < k:
            if curr is None:
                return head
            curr=curr.next
            count+=1

        next_head=self.reverseKGroup(curr,k)

        prev=next_head

        temp=head
        count=0

        while count<k:
            nxt=temp.next
            temp.next=prev
            prev=temp

            temp=nxt
            count+=1
        return prev        
        