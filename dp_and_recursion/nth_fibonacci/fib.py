def fib(n):
  # base case is 0 = 0, 1 = 1
  if n < 0:
    raise ValueError("No inputs less than 0 for fib")
  if n <= 1:
    return n

  memo = {}

  if n in memo:
    return memo[n]
  
  stored_result = fib(n - 1) + fib(n - 2)
  memo[n] = stored_result
  return stored_result  

class Fibber(object):
  def __init__(self):
    self.memo = {}
  
  def iter_fib(self, n):
    if n < 0:
      raise ValueError("no inputs less than 0 ")
    if n <= 1:
      return n
    
    for value in range(0, n + 1):
      if value in [0, 1]:
        self.memo[value] = value
      else:
        self.memo[value] = self.memo[value - 1] + self.memo[value - 2]
    
    return self.memo[n]
        

# Bottom-up and save space 
def iter_fib_save_space(n):
  if n < 0:
    raise ValueError("No inputs less than 0 for fib")
  if n <= 1:
    return n

  prev_prev = 0
  prev = 1
  for value in range(2, n + 1):
    current = prev_prev + prev
    prev_prev = prev 
    prev = current
  
  return prev