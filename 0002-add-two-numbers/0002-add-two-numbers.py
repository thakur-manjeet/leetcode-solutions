# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        add_node=dummy

        currA=l1
        currB=l2

        carry=0

        while currA or currB or carry:
            A=currA.val if currA else 0
            B=currB.val if currB else 0

            total=A+B+carry
            
            digit=total%10
            carry=total//10

            add_node.next=ListNode(digit)
            add_node=add_node.next

            if currA:
                currA=currA.next
            if currB:
                currB=currB.next


        return dummy.next            
        