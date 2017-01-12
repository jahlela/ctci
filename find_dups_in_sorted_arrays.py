def find_dups():
       """
   IN: arr1, arr2, which are sorted lists of ssids (ints)
   OUT: arr, which includes all ssids in both
   
   find_dups: [Int], [Int] -> [Int]

   m ≈ n - lengths are approximately the same:
      1. start both array idxs at 0
      2. walk through each arr, keeping those idxs as close as possible to one another, 
      3. Increment whichever's value is smaller
      4. save duplicates
   
                                   x                                     
   M: arr1 = [0, 1, 3, 4, 6, 8, 9, 10, 11,...,3000, 3005, 3007, 3008, 3009]  -> len1 = 7
   N: arr2 = [3000, 3005, 3007, 3008, 3009]        -> len2 = 5
                 x
   idx1 = 7
   idx2 = 5
   
   dups = [3, 8, 9]
   
   
   Solve and analyze the complexity for 2 cases:
   1. m ≈ n - lengths are approximately the same     -> O(N+M)
   2. m ≫ n - one is much longer than the other      -> O(NlogM)
   
   """
   dups = []

   idx1, idx2 = 0
   len1 = len(arr1)
   len2 = len(arr2)

   while idx1 < len1 and idx2 < len2:
       if arr1[idx1] == arr2[idx2]:
           dups.append(arr1[idx1])
           idx1 += 1
           idx2 += 1

        # Value in arr1 is smaller, increase idx1
       elif arr1[idx1] < arr2[idx2]:
           idx1 += 1

        # Value in arr1 is bigger, increase 1dx2
       elif arr1[idx1] > arr2[idx2]:
           idx2 += 1

        return dups

find_dups()


#O(n*logm) is better than O(n+m) if m is much larger than n


                                        
