Practical4
The score is 100 so I keep the original version.

Practical5
[Variable.py]: 
1. Wrong version: W = X + Y
2. Feedback: W is not a Boolean, it should be defined as 'X and Y'.
3. Respond:  Since W should be a Boolean variable and Booleans can be combined using “and”, so I changed the “+”into “and”. The meanings of “and” can be seen from truth tables from the lecture.

Practical5
[triangle.py]:
1. Wrong version: the pseudocode showed afterwards is too simple #initialize #use for loop to compute the first 10 values of sequence #running result
2. Feedback: Pseudocode could be more detailed and describe what the variable 'd' means
3. Respond: I enriched my pseudocode explaining all meanings of the variables. My polished version are as follows.  #d means the number of objects that can form an equilateral sequence and d is initialized to be 0. #Use for loop to compute the first 10 values of sequence. The nth triangle number is the number of dots or balls in a triangle with n dots on each side, which can be calculated as the sum of the n numbers from 1 to n.

Practical6
[Parental age vs offspring health]:
1. Wrong version: I create the dictionary by coding Paternal_age = {'30':1.03, '35':1.07, '40':1.11, '45':1.17, '50':1.23, '55':1.32, '60':1.42, '65':1.55, '70':1.72, '75':1.94}, but it cannot display correctly when the input changes.
2. Feedback: NOT displays frequency table that matches the input when the input table is changed
3. Response: To create a variable of the requested paternal age that can be modified, I use i variable to correspond the paternal age and chd. 
Here is the modified code.
dic = {}
for i in range(len(Paternal_age)):
dic[Paternal_age[i]] = chd[i]

Practical6: 
[Parental age vs offspring health]:
1. Wrong version: input a key in the code (i='50' print(Paternal_age[i]) without displaying frequency table according to the specific input
2. Feedback: It should contain a variable for age that can be modified and will return the correct risk of cardiovascular health in the offspring
3. Response: I rewrote the following code to print the risk of CHD for the offspring for a given paternal age from the input list.
a = input("Paternal age is ")
print("The risk of CHD in the offspring is "+str(dic[a]))

Practical6
[List manipulation]:
1. Wrong version: not display a well-labelled boxplot
2. Feedback: No labels
3. Response: add the y label of the boxplot using the code plt.ylabel('scores') and polish the boxplot to make it more clear


