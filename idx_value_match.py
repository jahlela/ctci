def find_idx_value_match(arr):
       """
   In: Array of sorted, distinct integers
   Out: Int, if idx and value match, -1 if not
   
   Look at n/2 element. 
   If idx == value, return value
   If value > idx, look at n/4, etc.
   If value < idx, look at 3n/4
   If we see no match, return -1
   """

          # If # of checks made == logn, return -1
          n = len(arr)
          checks = 0
          start_idx = 0
          end_idx = n - 1

          while checks < math.log(n): # start_idx < = end_index
              idx = (start_idx + end_idx) /2
              
              value = arr[idx]

              if idx == value:
                  return idx
            
              # Match could be in left
              if idx < value:
                  end_idx = idx - 1
                  checks += 1
                  
                  # Match could be in right
              elif idx > value:
                  start_idx = idx + 1
                  checks += 1
                  
              return -1
          
            
arr = [-1, 0, 3, 6]
arr2 = [-1, 0, 2, 4]

print find_idx_value_match(arr2)
        







                                                                                               
