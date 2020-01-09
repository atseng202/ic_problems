class Stack(object):

	def __init__(self):
	# """Initialize an empty stack"""
		self.items = []

	def push(self, item):
	# """Push a new item onto the stack"""
		self.items.append(item)

	def pop(self):
	# """Remove and return the last item"""
	# If the stack is empty, return None
	# (it would also be reasonable to throw an exception)
		if not self.items:
			return None

		return self.items.pop()

	def peek(self):
	# """Return the last item without removing it"""
		if not self.items:
			return None
		return self.items[-1]

class QueueTwoStacks(object):

# Implement the enqueue and dequeue methods
	def __init__(self):
	# Enqueue and dequeue using two stacks
		self.push_stack = Stack()
		self.pop_stack = Stack()

	def enqueue(self, item):   
		# if the push stack has any items, then enqueue onto it
		# if self.push_stack.peek():
		self.push_stack.push(item)

	def dequeue(self):
		if not self.push_stack.peek() and not self.pop_stack.peek():
			raise ValueError("Cannot dequeue from empty queue")
		
		if self.pop_stack.peek():
			first_item = self.pop_stack.pop()
			return first_item
		else:
			# nothing in the pop_stack so we need to look into push stack
			if not self.push_stack.peek():
				return None
			
			while self.push_stack.peek():
				item_to_move = self.push_stack.pop()
				self.pop_stack.push(item_to_move)
			
			return self.pop_stack.pop()

