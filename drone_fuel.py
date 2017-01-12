def drone(route):
   """
   IN: route, [3d coordinates]
   OUT: minimum fuel requirement to complete route
   
   drone: [dict] -> Int
   
   route = [{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}]
   
   X: Side to side (free movement)
   Y: Forward (free movement) 
   Z: Altitude (pay one liter for 1' increase, receive 1 liter for 1' decrease)
   
   Example:
   
   1st: {x:0, y:2, z:10} 
   2nd: {x:3, y:5, z:0}
   diff:  +3   +3   -10
         free  free -10 (fuel remaining = 10)
         
    
    [{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}] 
    z: 10 -> 0 -> 6 -> 15 -> 8
d alt    -10   +6   +9    -7
cost      10   -6   -9    7  
rem       10   4    -5    2
   
       x  x+10 x+4  x-5   x+2    

   10 -> 9 -> 8
  Find min from running total -> that's your answer, default to 0 if never negative
"""
   
   zc = [] # z coordinates
   
   for coordinate in route:
      zc.append(coordinate['z']) # check if needs to be 'z'
      
   rt = 0 # running total of fuel 
   min_seen = 0 
   idx = 0
   
   while idx < len(zc) - 1:
      rt -= zc[idx + 1] - zc[idx]
      min_seen = min(rt, min_seen)
      idx += 1
      
   return min_seen * -1
   

route = [{'x':0, 'y':2, 'z':10}, {'x':3, 'y':5, 'z':0}, {'x':9, 'y':20, 'z':6}, \
         {'x':10, 'y':12, 'z':15}, {'x':10, 'y':10, 'z':8}]
print drone(route)
