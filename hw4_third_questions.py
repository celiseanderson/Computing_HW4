# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:25:02 2021

@author: eande
"""

# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far
def total_registered_cases(data, country):
    return sum(data.get(country));
    

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(data):
    Per_Country = {};
    for key in data.keys():
        Per_Country[key] = total_registered_cases(data, key);
    return Per_Country;

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data):
    Per_Country = total_registered_cases_per_country(data);
    x = 0;
    country = '';
    for key, value in Per_Country.items():
        if value >= x:
            x = value;
            country = key;
    return country;