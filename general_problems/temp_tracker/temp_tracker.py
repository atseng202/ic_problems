class TempTracker(object):

  # Implement methods to track the max, min, mean, and mode
  def __init__(self):
    self.max = None
    self.min = None
    self.sum = 0
    self.count = 0
    self.modes = {}
    self.most_frequent = None

  def insert(self, temperature):
    self.sum += temperature
    self.count += 1
    if not temperature in self.modes:
      self.modes[temperature] = 1
    else:
      self.modes[temperature] += 1

    if not self.most_frequent:
      self.most_frequent = temperature
    elif self.modes[temperature] > self.modes[self.most_frequent]:
      self.most_frequent = temperature

    if not self.max and not self.min:
      self.max = temperature
      self.min = temperature
    
    if temperature > self.max:
      self.max = temperature
    
    if temperature < self.min:
      self.min = temperature

  def get_max(self):
    return self.max

  def get_min(self):
    return self.min

  def get_mean(self):
    if self.count == 0:
      return None
    return float(self.sum / self.count)

  def get_mode(self):
    if not self.most_frequent:
      return None
    return self.most_frequent


