class Queue {
  constructor() {
    this.queue = [];
    this.size = 0;
  }

  enqueue(item) {
    this.queue.unshift(item);
    this.size += 1;
  }

  dequeue() {
    this.size -= 1;
    return this.queue.pop();
  }
}

function getPath(graph, startNode, endNode) {

  // Find the shortest route in the network between the two users
  // using BFS I can get to the endNode with the shortest path, at the cost of space O(n)
  // to backtrack, I can use an object to keep track of each node's parent node, starting with the root with a null parent
  if (!graph[startNode]) {
    // throw error that startNode is not in our network
    throw new ValueError("Start node not in network");
  }
  if (!graph[endNode]) { 
    throw new ValueError("End node not in network");
  }

  const queue = new Queue();
  queue.enqueue(startNode);

  const prevNodes = { startNode: null};

  let currNode; 

  while (queue.size > 0) {
    currNode = queue.dequeue();
    if (currNode === endNode) { break; }

    const neighbors = graph[currNode];
    neighbors.forEach( neighbor => {
      if (!prevNodes[neighbor]) {
        // our object has not visited this neighbor yet
        prevNodes[neighbor] = currNode;
        queue.enqueue(neighbor);
      }
    });
  }

  if (currNode !== endNode) {
    // have no path to the endNode so return null
    return null;
  }

  // backtrack here
  const path = [currNode];
  while (currNode !== startNode) {
    currNode = prevNodes[currNode];
    path.push(currNode);
  }
  path.reverse();
  return path;
}