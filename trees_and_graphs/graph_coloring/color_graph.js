class GraphNode {
  constructor(label) {
    this.label = label;
    this.neighbors = new Set();
    this.color = null;
  }
}

function colorGraph(graph, colors) {


  // Create a valid coloring for the graph
  // each item in the graph is a GraphNode, with a label, set of neighbor nodes, and unset color
  // this function will give a valid color to each node
  // each node can have maximum degree of D, and thus only D + 1 colors can be used
  // Iterate thru the graph array, and with each node, check its neighbors (which should be at most D neighbors)
  // then iterate thru the colors array and check that the current color is not in the set of neighbor's colors, and use it
  for (let node of graph) {
    let neighbors = node.neighbors;
    
    if (neighbors.has(node)) {
      throw new ValueError("Cannot have self as neighbor");
    }
    // I can improve the solution here with a Set instead of array
    // Need to build the set my iterating thru neighbors set and building a temp D number set of colors
    let illegalNeighborColors = new Set();
    neighbors.forEach(neighbor => {
      if (neighbor.color && !illegalNeighborColors.has(neighbor.color)) {
        illegalNeighborColors.add(neighbor.color);
      }
    });
    // let neighborColors = [...neighbors].map( (neighborNode) => {
    //   return neighborNode.color;
    // })

    // only need to check D + 1 colors, where D is the number of neighbors
    const maxColors = neighbors.size + 1;
    for (let i = 0; i < maxColors; i++) {
      const currentColor = colors[i];
      if (illegalNeighborColors.has(currentColor)) {
        continue;
      } else {
        node.color = currentColor;
        break;
      }
    }

    // console.log("Neighbor colors below for node", node.label)
    // console.log(neighborColors);

  }
}

const colors = ['red', 'green', 'blue', 'orange', 'yellow', 'white'];
let graph = [];
{
  const nodeA = new GraphNode('A');
  const nodeB = new GraphNode('B');
  const nodeC = new GraphNode('C');
  const nodeD = new GraphNode('D');
  nodeA.neighbors.add(nodeB);
  nodeB.neighbors.add(nodeA);
  nodeB.neighbors.add(nodeC);
  nodeC.neighbors.add(nodeB);
  nodeC.neighbors.add(nodeD);
  nodeD.neighbors.add(nodeC);
  graph = [nodeA, nodeB, nodeC, nodeD];
}
colorGraph(graph, colors);
console.log(graph);