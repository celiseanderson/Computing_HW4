# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:32:39 2021

@author: eande
"""

###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed covid cases among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

#import pandas
import pandas as pd


#functions are defined here
def print_data(df, x):
    #initializing 
    Countries = []; #list of countries with over x cases
    Dead = 0; #Counting variable for dead
    Confirm = 0 #Counting variable for confirmed
    
    #iterating over data frame rows and columns
    for row, col in df.iterrows():
        if int(col[4]) > x: #if active cases over x cases
            Dead += col[2]; #Add their dead value to the counter
            Confirm += col[1]; #Add their confirmed value to the counter
            Countries.append(col[0]); #Add the country name to the list of countries

    #Since our dead and confirmed counters have total values not averages,
    #we divide by the length of the countries list to get the average
    Dead = Dead/len(Countries); 
    Confirm = Confirm/len(Countries);
    
    #Print the list of countries with over 500 active cases, their average dead, and their average confirmed
    print("\n List of Countries with ", x, " cases: ", Countries);
    print("Average dead for countries with", x, " cases: ", Dead);
    print("Average confirmed cases for countries with ", x, " cases:", Confirm)


#Now our main code starts
#import our data frame
df = pd.read_csv("covid.csv");
print("\nPrinting original:\n", df.head());

#call print_data function for over 500 cases
print_data(df, 500);
#call print_data function for over 1000 cases
print_data(df, 1000);
#call print_data function for over 5000 cases
print_data(df, 5000);




        

