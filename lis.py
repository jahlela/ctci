
def lis(arr):
    """
    IN: arr, an array of unsorted integers
    OUT: the longest increasing subsequence that can be made from arr

    lis: [Int] -> Int
    
    >>> arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    6
    >>> arr = [5]
    1
    >>> arr = []
    0

    """

    counts = [1]*len(arr)

    # Start two from arr[-2], because arr[-1] is guaranteed to be 1, and work backwards    
    for i in xrange( len(arr) -2, -1, -1):
        possibles = []
        # Check if head is less than each value that follows it
        for j in range(i+1,len(arr)):
            # Check if head is less than each value that follows it
            if arr[i] < arr[j]:
                # If so, add the count at that index to possible_counts
                possibles.append(1 + counts[j])
                
        # Update counts at i to be the max of possible lengths        
        counts[i] = max(possibles)
        
    # Answer is the maximum possible subsequence from counts
    return max(counts)



    
