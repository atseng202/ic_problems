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

function findSecondLargest(treeRoot) {

  // Find the second largest item in the binary search tree
  // I need to find the largest item first which is the rightmost node
  let currNode = treeRoot;
  let prevNode;

  // first get the final aka largest node to the right
  // then get the largest node that is not this one
  while (currNode.right) {
    prevNode = currNode;
    currNode = currNode.right;
  }

  // currNode is the largest node
  // now prevNode is the node right before it or undefined if currNode is the root
  if (!prevNode && treeRoot.left) {
    // currNode is currently our treeRoot and prevNode is undefined
    prevNode = currNode.left;

    // now prevNode is our starting point
    // from there get the largest value 
    while (prevNode.right) {
      prevNode = prevNode.right;
    }

    return prevNode.value;
  } else {
    // there is a previousNode and currNode is the largest value
    // prevNode's right node is currNode
    // prevNode's left node is smaller than prevNode so no need to check
    // but what about currNode's left child if it exists?
    if (currNode.left) {
      // there is a left child of the current node and it must be bigger than our prevNode since it is to the right
      // of our prevNode
      let currNodeLeft = currNode.left;
      while (currNodeLeft.right) {
        currNodeLeft = currNodeLeft.right;
      }
      return currNodeLeft.value;   
    } else {
      // no left child of currNode, therefore prevNode is the largest 2nd value
      return prevNode.value;
    }

  }
}

let treeRoot = new BinaryTreeNode(50);
let leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
let rightNode = treeRoot.insertRight(70);
rightNode.insertLeft(60);


treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
rightNode = treeRoot.insertRight(70);
leftNode = rightNode.insertLeft(60);
leftNode.insertRight(65);
leftNode = leftNode.insertLeft(55);
leftNode.insertRight(58);

console.log(findSecondLargest(treeRoot));