def find_second_largest(root_node):
    if not root_node.left and not root_node.right:
      raise ValueError("Only 1 node")

    # Find the second largest item in the binary search tree
    largest_node = root_node
    second_largest_node = None

    while largest_node.right:
      second_largest_node = largest_node
      largest_node = largest_node.right 

    # Two cases
    # 1. largest node had no right node (it is the root)
    # 2. largest node is the rightmost node, second_largest_node is node before it
    if largest_node.left:
      second_largest_node = largest_node.left

      while second_largest_node.right:
        second_largest_node = second_largest_node.right
      
      return second_largest_node.value
    else: 
      # no left node
      return second_largest_node.value



# Update: refactored the bottom code since I just have to check for the rightmost node's left child's rightmost node
# regardless of whether its at the root or some random depth
    # if not second_largest_node and largest_node: 
    #   # case 1: largest node is at root 
    #   if largest_node.left:
    #     second_largest_node = largest_node.left
        
    #     while second_largest_node.right:
    #       second_largest_node = second_largest_node.right

    #     return second_largest_node.value

    #   # otherwise, there is no second node and return None
    #   raise ValueError('No second node')
    # else:
    #   # case 2: largest node found, second_largest_node is right before it
    #   # Check if the rightmost node has a left child, and that left child's rightmost child node is the 2nd largest
    #   if largest_node.left:
    #     second_largest_node = largest_node.left

    #     while second_largest_node.right:
    #       second_largest_node = second_largest_node.right

    #     return second_largest_node.value
    #   else: 
    #     # no left child of largest node
    #     # second_largest_node is the value
    #     return second_largest_node.value 
      
    

