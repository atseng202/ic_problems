class BinaryTreeNode(object):

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert_left(self, value):
    self.left = BinaryTreeNode(value)
    return self.left

  def insert_right(self, value):
    self.right = BinaryTreeNode(value)
    return self.right

def is_binary_search_tree(root):

  # Determine if the tree is a valid binary search tree
  # Using DFS is better if the tree is balanced since a depth will be O(lgn)
  # First I need to set up a stack containing my root
  # While the stack is not empty, the last in node will be popped
  # and I will examine if it is a valid node, aka if it has any left or right nodes, that each one obeys 
  # its boundaries

  # The tuple will contain the lower_bound and upper_bound at the first and second indices for the node
  # Root node has no lower and upper bound so I placed None there
  tree_stack = [(root, None, None)]

  while len(tree_stack):
    curr_node, lower_bound, upper_bound = tree_stack.pop()

    if curr_node.left:
      # check that left node is a valid node
      # left node value should be less than upper bound which is curr_node value
      # AND greater than the lower bound given by curr_node
      left_node = curr_node.left
      if left_node.value > curr_node.value or (lower_bound and left_node.value < lower_bound):
        return False
      # passed condition, so add child node to the stack
      tree_stack.append((left_node, lower_bound, curr_node.value))
    
    if curr_node.right:
      #same as above, check that right node is valid
      # Right node value should be > than lower bound aka curr_node value 
      # AND lesser than the upper bound given by curr_node
      right_node = curr_node.right 
      if right_node.value < curr_node.value or (upper_bound and right_node.value > upper_bound):
        return False
      tree_stack.append((right_node, curr_node.value, upper_bound))
  
  return True


