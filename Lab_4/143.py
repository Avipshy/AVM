class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        head_1, head_2 = head, prev
        while head_2:
            temp1, temp2 = head_1.next, head_2.next
            head_1.next = head_2
            head_2.next = temp1
            head_1, head_2 = temp1, temp2
        