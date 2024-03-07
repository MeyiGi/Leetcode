# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []

        while head:
            res.append(head.val)
            head = head.next

        res = res[len(res) // 2:]
        node = None

        while res:
            node = ListNode(res.pop(), node)

        return node