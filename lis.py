
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

    # Start from arr[-2], because arr[-1] is guaranteed to be 1, then work backwards    
    for i in xrange( len(arr) -2, -1, -1):
        max_seen = 1
        
        for j in range(i+1,len(arr)):
            # Check if head is less than each value that follows it
            # Update max_seen if the new count is larger
            if arr[i] < arr[j]:
                max_seen = max(1 + counts[j], max_seen)
                
        # Update counts at i to be max possible length seen
        counts[i] = max_seen
        
    return max(counts)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print lis(arr)
