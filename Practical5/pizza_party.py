#initialize the values
p=0
n=1
#set the output sentenses using string
w1="I cut the pizza "
w2=" times, "
w3=" pieces of pizzas can be gotten."
#use for loop to get the each result
for n in range(1,25):
#at least the pizza should be cut one time     
      if n>=1:
#get the pieces value according to n
           p=((n**2)+n+2)/(2)
#get the oucome in sentenses
           print(w1+str(n)+w2+str(p)+w3)
#continue the loop          
           n=n+1
#if the pieces reach 64, everyone can eat a pieces of pizza,so loop breaks.     
      if p>=64:
           break
#after running the code, we find that 11 cuts result in 67 pieces.
