def is_valid(code):

  # Determine if the input code is valid
  open_stack = []
  opening_chars = ["(", "{", "["]
  opening_count = 0
  
  for idx in range(0, len(code)):
    char = code[idx]
    
    if char in opening_chars:
      open_stack.append(char)
      opening_count += 1
    else:
      # char is a closing char
      if len(open_stack) == 0:
        return False

      last_opening_char = open_stack.pop()
      opening_count -= 1
      if last_opening_char == "(" and char != ")":
        return False
      if last_opening_char == "{" and char != "}":
        return False
      if last_opening_char == "[" and char != "]":
        return False
    
  
  return opening_count == 0
