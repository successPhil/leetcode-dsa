


# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
    
    
    #Print head to see what is in memory address
    current = head
    while current:
        print(current.val)
        current = current.next

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)

node1.next = node2
node2.next = node3

print(deleteDuplicates(node1))