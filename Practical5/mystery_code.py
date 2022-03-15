# What does this piece of code do?
# Answer:maybe the code is to produce a random number from 1 to 99
# to get the number from the database
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#set a variable progress make sure the code running properly
progress=0
while progress<10:
	progress+=1
#to catch the n value from 1 to 99 randomly
	n = randint(1,100)

print(n)
