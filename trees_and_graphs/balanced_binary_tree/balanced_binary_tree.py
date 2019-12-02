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

def is_balanced(tree_root):

  # Determine if the tree is superbalanced
  # the same as before, i keep track of a min and max depth
  # using DFS: I will get the depths everytime I hit a leaf
  # Once I have a min and max depth, I can then check for the difference and return false early if that diff is > 1           
  min_depth = None
  max_depth = None
  current_depth = 0

  nodes_stack = [(tree_root, 0)]
  depths = []

  while (len(nodes_stack) > 0):
    latest_node_info = nodes_stack.pop()
    latest_node = latest_node_info[0]
    latest_depth = latest_node_info[1]

    if not latest_node.left and not latest_node.right:
      # this is a leaf node
      # Check the depth before we do anything else
      try:
        matching_depth = depths.index(latest_depth)
      except ValueError:
        matching_depth = None
  
      # we don't need to add the same depth twice, since that means there are multiple 
      # leaves with the same depth and this is okay
      # we do want to add depths that are different 
      if matching_depth == None:
        # there is no matching depth, so add our latest depth into the list
        depths.append(latest_depth)

      # Now evaluate the current depths list for any problems like 
      # 1. there are 3 different depths: this is not okay
      # 2. there are exactly 2 depths, and their difference is greater than 1
      if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
        return False
    else:
      # this is not a leaf node, add its children into the stack
      if latest_node.left:
        nodes_stack.append((latest_node.left, latest_depth + 1)) 
      
      if latest_node.right:
        nodes_stack.append((latest_node.right, latest_depth + 1))
    

  return True


tree = BinaryTreeNode(1)
left = tree.insert_left(5)
right = tree.insert_right(9)
right.insert_left(8)
right.insert_right(5)
print(is_balanced(tree))