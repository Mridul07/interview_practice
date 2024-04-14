# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        end_pointer = head
        dummy = ListNode()
        dummy.next = head

        for i in range(n):
            end_pointer = end_pointer.next
        
        prev_pointer = dummy

        while end_pointer:
            end_pointer = end_pointer.next
            prev_pointer = prev_pointer.next

        prev_pointer.next = prev_pointer.next.next

        return dummy.next