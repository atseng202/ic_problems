def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    # Get all the products before an index and all the products after an index
    if len(int_list) < 2:
      raise ValueError("Need more than 1 integers to get products except at index")

    list_length = len(int_list)

    productBeforeSoFar = 1
    productsBeforeIndex = []
    for i in range(list_length):
      productsBeforeIndex.append(productBeforeSoFar)
      productBeforeSoFar *= int_list[i]
    
    productAfterSoFar = 1
    for i in range(list_length - 1, -1, -1):
      productsBeforeIndex[i] *= productAfterSoFar
      productAfterSoFar *= int_list[i]
    
    return productsBeforeIndex


arr =  [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(arr))