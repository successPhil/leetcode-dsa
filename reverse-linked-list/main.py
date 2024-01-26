# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


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

# print(reverseList(node1).val)
reversed_head = reverseList(node1)

while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next


# print(reverseList(head).val)
# while reversed_head:
#     print(reversed_head.val)
#     reversed_head = reversed_head.next

# reversed_list.next
# print(reversed_list.val)




# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
        