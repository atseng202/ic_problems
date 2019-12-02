class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insertLeft(value) {
    this.left = new BinaryTreeNode(value);
    return this.left;
  }

  insertRight(value) {
    this.right = new BinaryTreeNode(value);
    return this.right;
  }
}

// I used BFS, but for purposes of this question, DFS reaches depths quicker
// and might be better for quickly comparing a max and min depth
// going to implement a depth-first version in python as practice
function isBalanced(treeRoot) {

  // Determine if the tree is superbalanced
  // visit every node, make sure to update the min and max depth after every child
  // using bfs is easier for iterative approach
  let currentDepth = 0;
  let minLeafDepth;
  let maxLeafDepth = 0;
  const queue = [treeRoot];

  while (queue.length > 0) {
    let nodesCountAtCurrentDepth = queue.length;

    while (nodesCountAtCurrentDepth > 0) {
      const nodeAtCurrentDepth = queue.shift();

      if (!nodeAtCurrentDepth.left && !nodeAtCurrentDepth.right) {
        // this is a leaf
        // check the current depth and update the min and max
        if (!minLeafDepth) {
          minLeafDepth = currentDepth;
        } else {
          minLeafDepth = Math.min(minLeafDepth, currentDepth);
        }

        if (currentDepth > maxLeafDepth) {
          maxLeafDepth = currentDepth;
        }
      }
      
      // add the child nodes
      if (nodeAtCurrentDepth.left) { queue.push(nodeAtCurrentDepth.left); }
      if (nodeAtCurrentDepth.right) { queue.push(nodeAtCurrentDepth.right); }

      nodesCountAtCurrentDepth -= 1;
    }

    // queue updated with next depth of 1 etc. from root of 0
    currentDepth += 1;
    



  }

  return (maxLeafDepth - minLeafDepth <= 1);

}
