class LinkedListNode(object):

  def __init__(self, value):
    self.value = value
    self.next = None


def contains_cycle(first_node):
  if not first_node or not first_node.next:
    #empty list or only 1 node
    return False

  curr_node = first_node
  slow_node = first_node
# while not curr_node and not curr_node.next:
  while curr_node:
    # if curr_node in nodes:
    curr_node = curr_node.next.next
    slow_node = slow_node.next

    if curr_node == slow_node:
      return True

  return False


fourth = LinkedListNode(4)
third = LinkedListNode(3)
second = LinkedListNode(2)
first = LinkedListNode(1)

third.next = fourth
second.next = third
first.next = second

print(contains_cycle(first))
