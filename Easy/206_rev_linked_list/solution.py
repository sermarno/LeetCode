###################
### 206. Reverse Linked List
### Given the head of a singly linked list, reverse the
### list, and return the reversed list.
###################

######################### CONCEPTS COVERED #########################
# CUSTOM PROVIDED DATA STRUCTURE
# RECURSION

# importing all commonly-used modules
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    # defines a linked list node
    def __init__(self, val=0, next=None):
        self.val = val # val = data sorted in node
        self.next = next # next = reference to next node in list
        # E.g. ListNode(1, ListNode(2)) = 1 -> 2

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # node that will trail behind as reversing
        curr = head # curr note visited
        while curr: # loop until end of list
            next_node = curr.next # placeholder for next node
            curr.next = prev # reversing this link
            prev = curr # prev becomes curr node
            curr = next_node # curr node become next node saved earlier
        return prev
# helper function to build linked list
def build_linked_list(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head
# helper function to print list
def linked_list_to_list(head):
    return f"[{','.join(str(node.val) for node in iter_list(head))}]"

def iter_list(head):
    while head:
        yield head
        head = head.next 

s = Solution()
head = build_linked_list([1,2,3,4,5])
rev_head = s.reverseList(head)
print(linked_list_to_list(rev_head))