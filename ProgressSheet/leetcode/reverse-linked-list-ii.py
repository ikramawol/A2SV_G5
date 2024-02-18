# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        prev = None
        for _ in range(right - left + 1):
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext

        pre.next.next = curr
        pre.next = prev

        return dummyNode.next
