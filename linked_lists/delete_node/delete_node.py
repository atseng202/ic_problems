class LinkedListNode(object):

  def __init__(self, value):
    self.value = value
    self.next  = None

def delete_node(node_to_delete):
  # need the node to delete's prev node
  curr_node = node_to_delete
  next_node = node_to_delete.next

  if next_node:
    curr_node.value = next_node.value
    curr_node.next = next_node.next
  else:
    # next_node is None, aka curr_node is last_node
    # Imperfect solution so we could raise an exception that we are unable
    # to delete the last node
    raise ValueError("Unable to delete last node of linked list")

  