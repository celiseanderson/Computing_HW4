4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv_list: list, job_title: str):
    found_users = []
    for dictionary in cv_list:
        for key, value in dictionary.items():
            if job_title in value:
                found_users.append(dictionary['user'])
    return found_users


cv_list = [{'user': 'john', 'jobs': ['analyst', 'engineer', 'spy']},
           {'user': 'jane', 'jobs': ['finance', 'software', 'spy']},
           {'user': 'doe', 'jobs': ['spy', 'analyst']}]

print(has_experience_as(cv_list, "analyst"))


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv_list: list):
    result = dict()
    for dictionary in cv_list:
        for jobTitle in set(dictionary['jobs']):
            if jobTitle in result.keys():
                result[jobTitle] += 1
            else:
                result[jobTitle] = 1
    return result
print(job_counts(cv_list))


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(cvList: list):
    my_tuple = tuple()
    popular_list = job_counts(cvList)
    for key, value in popular_list.items():
        if len(my_tuple) == 0:
            my_tuple = (key, value)
        else:
            if value > my_tuple[1]:
                # Tuples are immutable, so I created a list first in order to update the value
                my_list = [key, value]
                my_tuple = tuple(my_list)
    # If there are 2 jobs with the same count number, the function will return just one of the 2
    return my_tuple
print(most_popular_job(cv_list))

