p=0
n=1
w1="I cut the pizza "
w2=" times, "
w3=" pieces of pizzas can be gotten."
for n in range(1,25):
      if n>=1:
           p=((n**2)+n+2)/(2)
           print(w1+str(n)+w2+str(p)+w3)
           n=n+1
      if p>=64:
            break
     
