# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

###########################################################################
## By making use of slow and fast pointers we can find the middle of     ##
## A linked list.                                                        ##
## We are iterating our fast pointer twice as fast as the slow pointer   ##
## When that pointer reaches the end, the slow pointer will be 1/2 as far##
###########################################################################

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None


# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node6 = ListNode(6)

# node1.next = node2
# node2. next = node3
# node3. next = node4
# node4.next = node5
# node5.next = node6
# node6.next = None

# Prints memory address of linked list.val shows beginning
# Rest of the list can be found with .next
print(middleNode(node1))