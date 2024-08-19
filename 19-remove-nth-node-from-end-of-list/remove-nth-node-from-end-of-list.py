# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        Listnode = ListNode(0)
        Listnode.next = head

        #two pointers:
        one = Listnode
        two = Listnode

        # Move first pointer n+1 steps ahead:
        for x in range(n + 1):
            one = one.next
        
        # Move both pointers until first reaches the end:
        while one is not None:
            one = one.next
            two = two.next
            
        #Remove by skipping the node:
        two.next = two.next.next

        return Listnode.next
        