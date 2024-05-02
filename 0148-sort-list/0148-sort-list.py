# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        curr = None
        if left.val < right.val:
            curr = left
            left = left.next
        else:
            curr = right
            right = right.next
        
        head = curr

        while (left is not None) and (right is not None):
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next
        rest = left if left is not None else right

        while rest is not None:
            curr.next = rest
            curr = curr.next
            rest = rest.next
        return head

    def sort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.middle(head)
        right = mid.next
        mid.next = None
        left = head
        left = self.sort(left)
        right = self.sort(right)
        return self.merge(left, right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sort(head)
        

        