
tri = [ [7],     
        [3,8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]]


#def is_none(v, st):
#    if v == None:
#        print st
#    return v

def ms(idx_tup = None):

    idx_tup = idx_tup or (0,0)
    height, dist = idx_tup


    if len(tri) == 1:
        current = tri[height][dist]        

        print 'result', current
        return current

    if height < len(tri):
        current = tri[height][dist]        
        left = (height+1, dist)
        right = (height+1, dist+1)
        
        if dist is tri[height][-1]:
            result = current
            print 'result', result
            return result + ms(left)

        result = current + max(ms(left), ms(right))
        print 'result', result
        return result

    return 0
    
print ms()




























    
    






































""" 
def get_max(triangle, idx = 0):

    if len(triangle[0]) == 1:
        return triangle[0][idx]

    current_line = trinagle[-1]
    
    line_max = max(current_line)
    idx = current_line[line_max].index()
    
    return max( get_max(triangle[:-1], idx) , get_max(triangle[:-1], idx+1)    )


"""
