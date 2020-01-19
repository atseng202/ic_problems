my_rectangle = {

  # Coordinates of bottom-left corner
  'left_x': 1,
  'bottom_y': 1,

  # Width and height
  'width': 6,
  'height': 3,

}

def find_overlap(point_one, length_one, point_two, length_two):
  highest_starting_point = max(point_one, point_two)
  lowest_end_point = min(point_one + length_one, point_two + length_two)
  if highest_starting_point >= lowest_end_point:
    return (None, None)
  
  overlap = lowest_end_point - highest_starting_point
  return (highest_starting_point, overlap)

def find_rectangular_overlap_improved(rect1, rect2):
  rect1_left_x, rect2_left_x = rect1['left_x'], rect2['left_x']
  rect1_width, rect2_width = rect1['width'], rect2['width']
  rect1_bottom_y, rect2_bottom_y = rect1['bottom_y'], rect2['bottom_y']
  rect1_height, rect2_height = rect1['height'], rect2['height']
  res = {
      'left_x': None,
      'bottom_y': None,

      # Width and height
      'width': None,
      'height': None,
  }
  
  x_overlap_point, x_overlap_width = find_overlap(rect1_left_x, rect1_width, rect2_left_x, rect2_width)
  y_overlap_point, y_overlap_height = find_overlap(rect1_bottom_y, rect1_height, rect2_bottom_y, rect2_height)
  if not x_overlap_point or not y_overlap_point:
    return res

  return {
      'left_x': x_overlap_point,
      'bottom_y': y_overlap_point,

      # Width and height
      'width': x_overlap_width,
      'height': y_overlap_height,
  }

def find_x_overlap2(rect1, rect2):
  # 4 range possibilities 
  # They overlap when one range is contained in another or part of 1 range is in another
  # Find the highest_starting_point and lowest_end_point which will be our range
  rect2_right_x = rect2['left_x'] + rect2['width']
  rect1_right_x = rect1['left_x'] + rect1['width']
  rect1_left_x = rect1['left_x']
  rect2_left_x = rect2['left_x']
  highest_starting_point = max(rect1_left_x, rect2_left_x)
  lowest_end_point = min(rect1_right_x, rect2_right_x)
  if highest_starting_point >= lowest_end_point:
    return (None, None)
  
  overlap = lowest_end_point - highest_starting_point
  return (highest_starting_point, overlap)



def find_x_overlap(rect1, rect2):
  rect2_right_x = rect2['left_x'] + rect2['width']
  rect1_right_x = rect1['left_x'] + rect1['width']
  rect1_left_x = rect1['left_x']
  rect2_left_x = rect2['left_x']
  # Edge cases, they don't overlap
  if rect1_right_x <= rect2_left_x:
    return None
  elif rect2_right_x <= rect1_left_x:
    return None

  if rect1_left_x <= rect2_left_x:
    return rect2_left_x
  else:
    return rect1_left_x
  
def find_y_overlap(rect1, rect2):
  rect2_top_y = rect2['bottom_y'] + rect2['height']
  rect1_top_y = rect1['bottom_y'] + rect1['height']
  rect1_bottom_y = rect1['bottom_y']
  rect2_bottom_y = rect2['bottom_y']

  if rect1_top_y <= rect2_bottom_y or rect2_top_y <= rect1_bottom_y:
    return None
  
  if rect1_bottom_y <= rect2_bottom_y:
    return rect2_bottom_y
  else:
    return rect1_bottom_y


def find_rectangular_overlap(rect1, rect2):
  res = {
    'left_x': None,
    'bottom_y': None,

    # Width and height
    'width': None,
    'height': None,
  }
  if not find_x_overlap(rect1, rect2) or not find_y_overlap(rect1, rect2):
    return res
  

  # Calculate the overlap between the two rectangles
  # one of the vertices will belong to one of the triangles
  # if rect1 bottom y is below or eq to rect2 bottom y, we can assume that rect2 bottom vertex is used
  # otherwise, rect2 top vertex is used
  # res = {}
  rect2_top_y = rect2['bottom_y'] + rect2['height']
  rect1_top_y = rect1['bottom_y'] + rect1['height']
  rect2_right_x = rect2['left_x'] + rect2['width']
  rect1_right_x = rect1['left_x'] + rect1['width']

  if rect1['bottom_y'] <= rect2['bottom_y']:
    # use rect2 bottom_y, as rect2 overlaps with rect1
    bottom_diff = rect2['bottom_y'] - rect1['bottom_y']
    # If rect2 reaches past or equal to the max of rect1's height, then we can take the difference of rect1 height and bottom_diff
    # otherwise, the height is just the height of rect2
    intersection_height = None
    if rect2_top_y >= rect1_top_y:
      intersection_height = rect1['height'] - bottom_diff
    else:
      # rect2 top y is less than rect1 top y so we can assume the height is just rect2 height
      intersection_height = rect2['height']

    res['bottom_y'] = rect2['bottom_y']
    res['height'] = intersection_height
  else:
    # use rect1 bottom_y 
    bottom_diff = rect1['bottom_y'] - rect2['bottom_y']
    intersection_height = None
    if rect1_top_y >= rect2_top_y:
      intersection_height = rect2['height'] - bottom_diff
    else:
      intersection_height = rect1['height']
    
    res['bottom_y'] = rect1['bottom_y']
    res['height'] = intersection_height

  
  if rect1['left_x'] <= rect2['left_x']:
    # Rect2 overlaps with rect1
    left_diff = rect2['left_x'] - rect1['left_x']
    # Take first rect width - difference bc we are interesecting with the first rectangle 
    intersection_width = None
    if rect2_right_x >= rect1_right_x:
      intersection_width = rect1['width'] - left_diff
    else:
      intersection_width = rect2['width']

    res['left_x'] = rect2['left_x']
    res['width'] = intersection_width
  else:
    # Use rect1 left_x and width of rect2
    left_diff = rect1['left_x'] - rect2['left_x']
    intersection_width = None

    if rect1_right_x >= rect2_right_x:
      intersection_width = rect2['width'] - left_diff
    else:
      intersection_width = rect1['width']

    res['left_x'] = rect1['left_x']
    res['width'] = intersection_width
  
  return res
