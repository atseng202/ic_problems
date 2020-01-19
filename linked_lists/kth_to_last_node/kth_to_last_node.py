class LinkedListNode:

  def __init__(self, value):
    self.value = value
    self.next = None

def kth_to_last_node_improved(k, head):
  if k < 1: 
    raise ValueError("K cannot be 0")

  fast_walker = head
  slow_walker = head
  for i in range(1, k):
    if not fast_walker.next:
      raise ValueError("K cannot be larger than length of list")
    fast_walker = fast_walker.next
  
  # if fast_walker == None:
    # K is too big
    # raise ValueError("K cannot be larger than the length of the list")

  while fast_walker.next:
    slow_walker = slow_walker.next
    fast_walker = fast_walker.next
  
  return slow_walker

def kth_to_last_node(k, head):

  # Return the kth to last node in the linked list
  # if k == 1, that would be the last node, 2 equals second to last and so on
  if k < 1 or head == None:
    return None
  
  # It would help to know the length of our list, but assuming we don't know, and want to do it in O(n) time
  # I might use a fast walker to get the length
  fast_walker = head
  list_length = 1
  while fast_walker and fast_walker.next:
    fast_walker = fast_walker.next.next
    list_length += 2
  if fast_walker == None:
    list_length -= 1
  
  # If length is 5, and k is 1, I need to step 5 - 1 times; if k is 2, step 5 - 2 = 3 times
  # Therefore I need to tep length - k times
  times = list_length - k
  curr_node = head
  while times > 0:
    curr_node = curr_node.next
    times -= 1
  return curr_node

  # return None
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node_improved(2, a).value)
