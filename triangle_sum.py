"""


7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

[    [7],     
     [3,8],
     [8, 1, 0],
     [2, 7, 4, 4],
     [4, 5, 2, 6, 5]]

    [0]
   [0,1]
  [0,1,2]
 [0,1,2,3]
[0,1,2,3,4]  

0 -> 0 or 1
1 -> 1 or 2
2 -> 2 or 3
3 -> 3 or 4

Sample Output
30

"""


def get_max(triangle, idx = 0):

    if len(triangle) == 1:
        return triangle[0][0]
    
    print 'idx', idx
    current_line = triangle[-1]
    print 'current_line', current_line

    idx = current_line.index(max(current_line))
    current_val = current_line[idx]
    
    print 'current_val', current_val
    
    if idx == len(current_line)-1:
        return current_val + get_max(triangle[:-1], idx-1)
    elif idx == 0:
        return current_val + get_max(triangle[:-1], idx)
    else:
        return current_val + max( get_max(triangle[:-1], idx) , get_max(triangle[:-1], idx-1) )


'''
def get_max(triangle, idx=0, cur = None):

    if len(triangle) == 1:
        return triangle[0][0]

    max(
    
'''



    



triangle = [[7],     
            [3,8],
            [8, 1, 0],
            [2, 7, 4, 4],
            [4, 5, 2, 6, 5]]

print get_max(triangle) - 1



