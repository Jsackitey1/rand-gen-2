
"""
A program to generate a specified number of random numbers in a given range

@author:Sackitey Joseph

""" 
    

import math    
import random

# generating random numbers within a specified min and max  values
min_value=int(input("\tEnter the min Value: ",))
max_value= int(input("\tEnter the max value: "))
# this is store the total executions ,thus the possible number of random numbers
total_executions= int(input("\tEnter the number of executions: ",))
# to store the execution counts
execution=0
# a list to store all generated random numbers
execution_list= []
# a list to store the number of times each number is generated
number_count= []
# random numbers to be used 



expected_count= 0
expected_percent=0


# Using the while loop to generate random numbers 

while execution < total_executions :
    # Generate randm numbers from min to max value and save in random_numbers
    random_number= random.randint(min_value, max_value)
# all random numbers generated are dtoresd in this list execution_list    
    execution_list.append(random_number)
    execution+=1

# this counts the number of times each number is generated and store them in the number_count list

i= min_value
while i<= max_value:
       
    number_count.append(execution_list.count(i))     
     
    i+=1



expected_count = execution/(max_value-min_value +1)

expected_percent= 100/(max_value-min_value +1)



print("Random number analysis\n")
print(f"Range of executions:{min_value} to {max_value}\n")
print(f"Total executions: {total_executions}\n")
print("Equal distribution of random numbers")
print("\tExpected distribution:")
print(f"\t\tcount: {expected_count:.2f}")
print(f"\t\tpercent: {expected_percent:.2f}%")


print("\tAchieved distribution:")

for value, count in enumerate(number_count,min_value):
   percent = (count / execution) * 100
   print(f"\t{value}: {count}  -  {percent:.2f}%")
        