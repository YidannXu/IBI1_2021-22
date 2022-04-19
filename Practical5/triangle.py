#d means the number of objects that can form an equilateral sequence and d is initialized to be 0. 
d=0
#Use for loop to compute the first 10 values of sequence. The nth triangle number is the number of dots or balls in a triangle with n dots on each side, which can be calculated as the sum of the n numbers from 1 to n.
for i in range(1,11,1):
    d=d+i
    print (d) 
#Here shows the running result:
1
3
6
10
15
21
28
36
45
55
