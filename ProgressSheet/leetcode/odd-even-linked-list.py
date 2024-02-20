# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        even = head
        odd = even.next
        oddHead = odd
        while even.next and odd.next:
            even.next = odd.next
            odd.next = odd.next.next

            even = even.next
            odd = odd.next

        even.next = oddHead
        return head