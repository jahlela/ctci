#In how many ways can you tile a 3xn rectangle with 2x1 dominoes?

def dom(w):
    """
    """

    hole_top = [0, 1, 0]
    complete = [0, 0, 3]

    for i in range(3,w+1):
        hole_top_result = complete[i-1] + hole_top[i-2]
        hole_top.append(hole_top_result)

        complete_result = complete[i-2] + 2 * hole_top[i-1]
        complete.append(complete_result)

    return complete[w]
        
print '0:', dom(0)
print '1:', dom(1)
print '2:', dom(2)
print '3:', dom(3)
print '4:', dom(4)
print '8:', dom(8)





    
   


