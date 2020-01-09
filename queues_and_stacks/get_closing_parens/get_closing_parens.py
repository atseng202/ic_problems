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

# Two stacks
# Push left to left stack
# Everytime there's a right stack, pop out the top left item and see if its the corresponding open paren index
# I could just ignore the right stack tbh
# Edit: Instead of adding O(n) additional space with a push stack and popping it out to check if it is the corresponding
# open index to the closing index, I just keep track of the count of opening parens and also the position of my 
# opening parens in that count
# Then I can just check for matching position of that count and return the closing index if that's the case
# decrementing the opening parens count otherwise
def get_closing_paren(sentence, opening_paren_index):
  left_count = 0
  paren_count_pos = -1
  for idx, char in enumerate(sentence):
    if char == "(":
      left_count += 1

      if idx == opening_paren_index:
        paren_count_pos = left_count
    else:
      # This is a right parenthesis so check if left stack is the correct one
      if left_count == paren_count_pos:
        return idx
      left_count -= 1
 
  if left_count > 0:
    raise ValueError("No matching closing parens")

  return -1
  # otherwise no closing parens to match


actual = get_closing_paren('()()((()()))', 5)
print(actual)
