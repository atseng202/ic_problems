def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
  take_out_length = len(take_out_orders)
  dine_in_length = len(dine_in_orders)
  served_length = len(served_orders)
  if served_length != (take_out_length + dine_in_length): 
    return False 

  take_out_idx = 0
  dine_in_idx = 0 

  for order in served_orders:
    if take_out_idx < take_out_length and order == take_out_orders[take_out_idx]:
      take_out_idx += 1
    elif dine_in_idx < dine_in_length and order == dine_in_orders[dine_in_idx]:
      dine_in_idx += 1
    else:
      return False
  
  
  
  return True

takeOut = [1,3,5]
dineIn = [2,4,6]
served = [1, 2, 3, 5, 4, 6]
print(is_first_come_first_served(takeOut, dineIn, served))