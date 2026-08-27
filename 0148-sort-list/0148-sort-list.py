# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        slow =head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            prev=prev.next

        first_list=head
        prev.next=None
        second_list=slow

        sorted_first=self.sortList(first_list)
        sorted_second=self.sortList(second_list)

        merge_dummy=ListNode(0)
        sorted_list=merge_dummy

        while sorted_first and sorted_second:
            if sorted_first.val < sorted_second.val:
                sorted_list.next=sorted_first
                sorted_first=sorted_first.next
            else:
                sorted_list.next=sorted_second
                sorted_second=sorted_second.next
            sorted_list=sorted_list.next

        sorted_list.next= sorted_first if sorted_first else sorted_second

        return merge_dummy.next        