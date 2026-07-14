# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force:  loop through to get tail, create new linkedlist, and add nodes in reverse
        # 1. time complexity
        # 2. val and next
        # 3. the next value
        # 4. linked List
        # 5. first loop through to get tail
        
        # check for empty LL
        if head == None:
            return head

        # initialize tail
        tail = 0

        # loop through LL and set curr to tail
        curr = head
        while curr:
            tail = curr
            curr = curr.next

        # loop through LL while curr != tail and curr exists
        curr = head
        while curr != tail and curr:
            # add duplicate head to tail node
            tail.next = ListNode(curr.val, tail.next)
            curr = curr.next
                # set new head
        head = tail
        # return head
        return head