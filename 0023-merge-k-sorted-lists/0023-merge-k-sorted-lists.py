# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeKListHelper(lists,0,len(lists)-1)

    def mergeKListHelper(self,lists,start,end):
        if start == end:
            return lists[start]

        if start + 1 == end:
            return self.merge2List(lists[start],lists[end])

        mid= (start+end) //2
        left= self.mergeKListHelper(lists,start,mid)
        right=self.mergeKListHelper(lists,mid+1,end)

        return self.merge2List(left,right)

    def merge2List(self,l1,l2):
        dummy=ListNode(0)
        curr=dummy

        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next

        curr.next=l1 if l1 else l2

        return dummy.next                                