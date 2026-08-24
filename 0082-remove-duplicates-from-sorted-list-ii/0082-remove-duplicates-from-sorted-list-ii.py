# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        sorted_list=dummy
        curr=head

        while curr:
            if curr.next!=None and curr.val == curr.next.val:
                while curr.next!=None and curr.val == curr.next.val:
                    curr=curr.next
                sorted_list.next=curr.next    
            else:
                sorted_list=sorted_list.next

            curr=curr.next

        return dummy.next                
