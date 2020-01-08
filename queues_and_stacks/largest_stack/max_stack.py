class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):

	def __init__(self):
		self.stack_items = Stack()
	
	def push(self, items):
		last_item_tuple = self.stack_items.peek()
		if not last_item_tuple:
			self.stack_items.push((items, items))
		else: 
			last_max_item = last_item_tuple[1]
			self.stack_items.push((items, max(items, last_max_item)))
	
	def pop(self):
		last_item_tuple = self.stack_items.pop()
		if not last_item_tuple:
			return None
		return last_item_tuple[0]
	
	def get_max(self):
		last_item_tuple = self.stack_items.peek()
		if not last_item_tuple:
			return None
		return last_item_tuple[1]
	
max_stack = MaxStack()
max_stack.push(5)

max_stack.push(4)
max_stack.push(7)
max_stack.push(7)
max_stack.push(8)
print(max_stack.get_max())
print(max_stack.pop())
print(max_stack.stack_items.items)
print(max_stack.get_max())
