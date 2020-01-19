
def reverse(head_of_list):

  # Reverse the linked list in place
  # next node will now point to curr node and curr node points to prev Node (None for head)
  # curr_node = head_of_list
  prev_node = None
  curr_node = head_of_list

  while curr_node:
    old_next = curr_node.next
    curr_node.next = prev_node

    prev_node = curr_node
    curr_node = old_next

  return prev_node 
  
class LinkedListNode(object):

  def __init__(self, value, next=None):
    self.value = value
    self.next  = next

first = LinkedListNode(1)
reverse(first)

print(first.value)
print(first.next)