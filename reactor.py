
1. Pick metric for breaking down problem
2. Name your recurrence relation something short and meaningful
3. Write your recurrence relation I/O. It should take one input (not a constant) and produce one output
4. Write the recurence relation type
5. Write recurrence relation
   a. Metric for breaking down the problem is function argument (change to be made)
   b. What choices do you have that you will iterate over?
   c. Output is the evaluation (minimum number of coins)
   d. What is this function doing? (max, min, sum, product, -- of what things)
   e. How do we get the value of the choices?
   f. Write the recurrence relation ---------- rr(argument) = ....
6. Write base cases
7. Prove that your function works by induction

f: domain -> image #range only applies to integers




You are to write a program which, given the positions of the villages and the number of post offices,
computes the least possible sum of all distances between each village and its nearest post office.

Input

Your program is to read from standard input. The first line contains two integers: the first is the number
of villages V, 1 <= V <= 300, and the second is the number of post offices P, 1 <= P <= 30, P <= V.
The second line contains V integers in increasing order. These V integers are the positions of the villages.
For each position X it holds that 1 <= X <= 10000.

Output

The first line contains one integer S, which is the sum of all distances between each village and
its nearest post office.


1. Breakdown by integer where the villages are on the highway
2. ms (minimum sum of post office distances)
3. INPUT: Takes as input a list of integers, which represent the positions of villages
   along a highway and a number of post offices
   OUTPUT: Returns the minimum sum of distances between each village and its nearest post office
4. ms: Int -> Int # (array -> Int?)
5.
   a. Break down by integer where the villages are on the highway
   b. Iterate over options for where to put post offices
   c. Find minimum sum of distances between each village and its nearest post office
   d. minimum sum
   e. minimum distance if we choose to put a post office here
   e. villages takes in an index i and outputs villages[i]
   e. global function villages: Int -> Int
   e. ms(p, i) = min { ms(p-1, i-1), ms(p-1, i) }

      i = end index for subsequence of array
      k = number of post offices
   e. ms(i, k) = ms(i-1, k-1) + ms(len(array), 1)
   # the minimum sum of array[k:]
   e. ms takes in i, the end index of a subsequence of the original array, and k, the number of post offices
      ms outputs the minimum sum, given the subsequence and number of post offices

   minimum sum of distances


   e. How do we get the value of the choices?
   e. What if we were changing both the number of villages and the number of post offices?

   - If we put one post office at the last village, and find the minimum for the n-1 villages
   - Make the invariant of the rr that it returns the minimum dist sum, provided that there is a po at the last village

   - p, villages -> min dist to put p (the #po), provided you have a po at the last village

   e. 

   f. Write the recurrence relation ---------- rr(argument) = ....



   e. get value of dom(n-1) if we choose stack, top, or bottom
   e. number of ways to tile rectangle, if we choose that option

      c(w)  = c(w-2) + 2 * ht(w-1)     # What are the ways to end with a complete column?
      ht(w) = c(w - 1)  + ht(w - 2)






6. Base: If # of post offices > # of villages, return 0
   Base: If #po = #villages + 1, return difference between two closest villages
   Ext: If #po = #v + 2, return sum of difference between two pairs of closest villages


   





Q: In how many ways can you tile a 3xn rectangle with 2x1 dominoes? 

1. Breakdown: n
2. Name: dom
3. In: n, the width of the rectangle (height = 3)
   Out: number of ways to tile a 3xn rectangle with 2x1 dominoes
4. dom: Int -> Int
5.
   a. breakdown by w, width of rectangle
   b. 3 options: three stacked, top vertical + horizontal, horizontal + bottom vertical
   c. number of ways to tile a 3xn rectangle with 2x1 dominoes
   d. count
   e. get value of dom(w-1) or dom(w-1) if we choose stack, top, or bottom
   e. number of ways to tile rectangle, if we choose that option

      c(w)  = c(w-2) + 2 * ht(w-1)     # What are the ways to end with a complete column?
      ht(w) = c(w - 1)  + ht(w - 2)
   
      
   f. dom(n) =


# Use a few mutually recursive recurrence relations

6. Base cases: 


Recurrence Relations for adding 2 columns
   3 Horizontal   ::  dom(n) = 1 + dom(n-2)
   2 Vertical + Top  ::  dom(n) = 1 + dom(n-2)
   2 Vertical + Bottom  ::  dom(n) = 1 + dom(n-2)
   

We'll have a rr for each combination of holes for each possibility
   
   Where are the possible gaps?

   What board state 

   1 hole or two holes (never just the hole in the middle)

     c    ft    fb    ht     hb
     1     1     0     0      1
     1     0     0     1      1
     1     0     1     1      0

 c:  Int -> Int        
 ft: Int -> Int
 fb: Int -> Int
 ht: Int -> Int
 hb: Int -> Int 

 c(w)  = c(w-2) + hb(w-1) + ht(w-1)     # What are the ways to end with a complete column?
 ft(w) = ht(w-1)                        # What are the ways to end with top filled?
 fb(w) = hb(w-1)
 ht(w) = c(w - 1)  + ft(w - 1)
 hb(w) = c(w - 1)  + fb(w - 1)

===>

 c(w)  = c(w-2) + 2 * ht(w-1)     # What are the ways to end with a complete column?
 ht(w) = c(w - 1)  + ht(w - 2)






▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ht(w)
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
              w 

==>

▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓       c(w-1)
▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             w - 1

or

▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓       ft(w-1)
▓▓▓▓▓▓▓▓▓▓▓▓▓
             w - 1 
              

 Each rr is the # of ways to tile a board of width w that ends in that pattern


 1   2 2
 1    


 2 2
 2 2  f(2) = 1
 2 2



 1 2 2 1
 1 2 2 1
 2 2 2 2

 2 2 2 2
 1 2 2 1
 1 2 2 1

 2 2 2 2
 2 2 2 2
 2 2 2 2

 1 1 2 2
 1 1 2 2 
 2 2 2 2

 2 2 2 2
 1 1 2 2
 1 1 2 2 

 2 2 2 2
 2 2 1 1
 2 2 1 1

 2 2 1 1
 2 2 1 1
 2 2 2 2

 1 1 1 1
 1 1 1 1
 2 2 2 2

 2 2 2 2
 1 1 1 1
 1 1 1 1

 2 2 2 2
 1 2 2 1
 1 2 2 1


 for 4 columns:

  2 | | | 
 1
 -
 -
 -
 





















 0 0 0 0
 0 0 0 0
 0 0 0 0

 2 2 2 2
 1 2 2 1
 1 2 2 1

 0 0 0 0
 0 0 0 0
 0 0 0 0

 0 0 0 0
 0 0 0 0
 0 0 0 0

 0 0 0 0
 0 0 0 0
 0 0 0 0


 0 0 0 0 0 0
 0 0 0 0 0 0
 0 0 0 0 0 0

 0 0 0 0 0 0
 0 0 0 0 0 0
 0 0 0 0 0 0






















   e. Get values of ms(height+1, dist) + running_total
                and ms(height+1, dist+1) + running_total



Q: Find max sum for triangle path, starting with top and moving down to the left or right and ending at the bottom

1. Breaking down by index into the triangle (sub-triangles)
2. Name: ms
3. Input: idx into triangle (height and dist from left)
   Output: maximum possible sum
4. ms: (Int,Int) -> Int
5.
   a. Break down by idx into triangle
   b. Options: left or right 
   c. Maximum sum
   d. Maximum
   e. Get values of ms(height+1, dist) + running_total
                and ms(height+1, dist+1) + running_total
   f. ms(height, dist) = val(height, dist) + max { ms(height+1, dist), ms(height+1, dist+1) }
6. Base: height == 1 or reached bottom





























Figure 1 shows a number triangle. Write a program that calculates the highest sum of numbers passed on a route that starts at the top
and ends somewhere on the base. Each step can go either diagonally down to the left or diagonally down to the right.

Input: Your program is to read from standard input. The first line contains one integer N: the number of rows in the triangle.
       The following N lines describe the data of the triangle. The number of rows in the triangle is > 1 but <= 100.
       The numbers in the triangle, all integers, are between 0 and 99.

Output: The highest sum is written as an integer.

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5


1. Break down by line in triangle
2. max_sum
3. Input: n lines of ints that build the triangle
   Output: maximum sum possible taking one value from each line, moving down left or right, diagonally
4. max_sum: array -> Int
5.
   a. Breakdown: Line of triangle
   b. Iterate: values in each line
   c. Evaluation: max sum from taking one value from each line
   d. 



Calculate the max value of the product of either f(x-2)*f(x-3) or f(x-1) + f(x-4)

f(x) = max { f(x-2)*f(x-3) or f(x-1) + f(x-4) }
f(0) = 1
f(1) = 20
f(2) = 25
f(3) = 45
f(4) = 50



1. A reactor in a certain chemical plant is shut down annually and either overhauled or
replaced. The cost of overhaul is related to the age of the reactor, as shown in the table
below. After 4 years the reactor has to be replaced.
Reactor’s age [years] 0 1 2 3
Cost of overhaul [$1000] 0 10 25 60
The cost of a new reactor is $100.000. The expected life of the whole plant is five years
starting with a new reactor. The management of the plant needs the policy for the
replacement of the reactor over the five-year period that minimizes total costs.
Result: Minimum cost $145,000, optima: (decisions at the ends of years 1 – 4)
 overhaul - overhaul - replace - overhaul
  overhaul - replace - overhaul - overhaul 



1. Break down by years
2. me "min expense"
3. me takes in the age of the plant and return the minimum expense to maintain the plant for that year
4. me: Int -> Int
5. 
   a. Breakdown metric: plant_age
   b. Iteration: overhaul or replace
   c. Evaluate: expense 
   d. Minimizing
   e. Overhaul at year y: cost(y) + me(y-1).
      Replace at year y:  100 + me(y - 1)
   f. me(y) = if y < 4 then min{ cost(y) + me(y-1), 100 + me(y - 1) }
                       else min{ cost(y) + me(y-1), 100 + me(y - 1) }
















SET BUILDER NOTATION = { x * 2 | x is a Int AND x > 5 }
MIN NOTATION = min{someset}

5. f(plant_age) = f(plant_age - 1) + min{ 1000 , cost(plant_age) }


5. f(age) =                                                
   a. Metric for breakdown: age of plant (stop at 5 years)
   b. f iterates on array of costs each year
   c. Minimize cost (and the replacement schedule)
6. Base case: if reactor age is 0 or if age of plant is 5: cost = 0
              if reactor age is 3: cost = 1000


Givens: 
* After 4 years, reactor must be replaced
* Cost of new reactor is $1,000
* Plant lifespan is 5 years








Break down by year
f takes in years --> minimum expenditure to maintain the reactor
f: Int -> Int
f(years) 
