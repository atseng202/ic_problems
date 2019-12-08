class GraphNode:

  def __init__(self, label):
    self.label = label
    self.neighbors = set()
    self.color = None


def color_graph(graph, colors):

  # Create a valid coloring for the graph
  # Iterate thru the N nodes
  # for each node, look at it's nearest neighbors
  # the total number of neighbors we would look at is 2 * M where M is the edges connecting two neighbors
  # with the neighbors, we will get the Set of colors that we cannot apply to our current node
  # then check our array of D colors, and if the color is not in the set, we can apply it to our current node

  # we have N Nodes
  for graph_node in graph:
    # at most D neighbors
    # over the span of the loop, we will have a total of 2M neighbors, where M is the edges between nodes
    neighbors = graph_node.neighbors

    # make sure graph node is not its own neighbor to prevent any loops
    if graph_node in neighbors:
      raise ValueError("A node cannot be its own neighbor")

    illegal_colors = set()
    for neighbor in neighbors:
      if neighbor.color:
        illegal_colors.add(neighbor.color)

    # make sure a color we choose is not in the set of illegal colors  
    for color in colors:
      if color not in illegal_colors:
        graph_node.color = color
        break
  
  return 0

