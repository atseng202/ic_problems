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

function isBinarySearchTree(treeRoot) {

  // Determine if the tree is a valid binary search tree
  // doing bfs is okay but at each node, I need to keep track of a lowerBound and upperBound
  // except at root
  // i.e. root.left (its lowerBound is nothing, upperBound is root.value)
  // every subsequent child's lowerbound for nodes to the right is the parent, 
  // every child's upperbound is the parent if it is to the left
  // so yes I can do BFS but might as well do dfs because the depth stored should be O(lgn)
  const nodes = [[treeRoot, undefined, undefined]];
  
  while (nodes.length > 0) {
    const currNodeInfo = nodes.pop();
    const currNode = currNodeInfo[0];
    const currLowerBound = currNodeInfo[1];
    const currUpperBound = currNodeInfo[2];
    
    if (currNode.left) {
      // child of this node
      // add it to array along with its lower and upper bound
      const leftNode = currNode.left;
      // this value should be less than currNode value
      if (leftNode.value > currNode.value || (currLowerBound && leftNode.value < currLowerBound)) { return false; }
      // upper bound is currNode
      // lower bound is currNode's lower bound
      const leftNodeInfo = [leftNode, currLowerBound, currNode.value];
      nodes.push(leftNodeInfo);
    }

    if (currNode.right) {
      const rightNode = currNode.right;
      // i must be bigger than this lower bound (parent node) and less than the upper bound which I get from parent
      if (rightNode.value < currNode.value || (currUpperBound && rightNode.value > currUpperBound)) { return false; }

      // lower bound is currNode value, upper bound is curr node's upper bound
      const rightNodeInfo = [rightNode, currNode.value, currUpperBound];
      nodes.push(rightNodeInfo);
    }
  }

  // checked the entire tree's values and nothing was wrong
  return true;
}

treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(20);
leftNode.insertRight(60);
rightNode = treeRoot.insertRight(80);
rightNode.insertLeft(70);
rightNode.insertRight(90);
isBinarySearchTree(treeRoot);