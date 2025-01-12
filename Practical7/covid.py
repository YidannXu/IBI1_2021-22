import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import the .csv file
os.chdir("/home/chengzijiang/macbook/IBI1_2021-22/Practical7") #marker can change the path here
covid_data=pd.read_csv("full_data.csv")

#show the first and third columns from rows 10-20
print(covid_data.iloc[9:20,0:3:2])

#use a Boolean to show "total_cases" for all rows corresponding to Afghanistan
my_columns = [False, False, False, False, True, False]
my_rows = []
for i in range(0,len(covid_data)):
  if covid_data.loc[i,"location"] == "Afghanistan":
     my_rows.append(True)
  else:
     my_rows.append(False)
print(covid_data.loc[my_rows,my_columns])

#compute the mean number of new cases and new deaths in China
#access the specific row and column values by loc- and iloc-function
china_new_data=covid_data.loc[covid_data["location"]=="China",["date","new_cases","new_deaths"]]
china_dates=china_new_data.iloc[:,0]
#calculate the mean number and print them
new_cases_mean=np.mean(china_new_data["new_cases"])
print("the mean number of new cases: ",new_cases_mean)
new_deaths_mean=np.mean(china_new_data["new_deaths"])
print("the mean number of new deaths: ",new_deaths_mean)

#creat a boxplot of new cases and new deaths in China worldwide
x1=china_new_data["new_cases"]
x2=china_new_data["new_deaths"]
plt.boxplot([x1,x2],labels=["new_cases","new_deaths"])
plt.title("the boxplot of new cases and new deaths in China worldwide")
plt.ylabel("number")
plt.show()

#plot both new cases and new deaths in China over time
china_data=covid_data.loc[covid_data["location"]=="China",["date","new_cases","new_deaths"]]
china_dates=china_data.loc[:,"date"]
new_cases=china_data.loc[:,"new_cases"]
new_deaths=china_data.loc[:,"new_deaths"]
plt.plot(china_dates,new_cases,"b*")
plt.plot(china_dates,new_deaths,"ro")
plt.xlabel("date")
plt.ylabel("number of people")
plt.legend(["new_cases","new_deaths"])
#make the x axis more clear and the code is from Practical7
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("New cases and new deaths in China over time")
plt.show()

#answer the question: When the new cases and total cases were significantly increasing in Spain?
Spain_data=covid_data.loc[covid_data["location"]=="Spain",["date","new_cases","total_cases"]]
Spain_dates=Spain_data.loc[:,"date"]
new_cases=Spain_data.loc[:,"new_cases"]
total_cases=Spain_data.loc[:,"total_cases"]
plt.plot(Spain_dates,new_cases,"b*")
plt.plot(Spain_dates,total_cases,"ro")
plt.xlabel("date")
plt.ylabel("number of people")
plt.legend(["new_cases","total_cases"])
#make the x axis more clear and the code is from Practical7
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.title("New cases and total cases in Spain over time")
plt.show()

