#!/usr/bin/env python
# coding: utf-8

# The first day of class was January 11th, 2021. Write code that shows how many
# days have elapsed between then and now, where "now" is the date someone runs
# your code. (Hint: look up the datetime standard Python library.)
# from datetime import timedelta
from datetime import date
#from random import Random

first_day = date(2021, 1, 11)
today = date.today()
days_elapsed = today - first_day

print("Today:", today)
print("First Day:", first_day)
print(days_elapsed.days, "days")

# Write code that begins with a Python list, containing some number of integers
# or floats.
numbers = [1,2,3,4,5]
print(numbers)

# - Multiply each value by 2. (Hint: look up list comprehensions)
doubled_numbers = [2*x for x in numbers]

# - Remove all odd numbers
even_numbers = [x for x in doubled_numbers if x%2==0]

# - Print a random value from the resulting list. (Hint: look up the random 
# standard Python library.)
print(random.choice(even_numbers))

# Write a Python function that takes a string as an argument, then returns a 
# modified string. Your function should:
# - First, test that the argument is a string, and that its length is at least 
# 15 words. (Hint: look up the assert, isinstance, and len standard Python 
# functions, and the split string method.)

def ValidateString (submission):
    assert (isinstance(submission, str)), "Error: Input not a string"
    assert (len(submission) >= 15), "Error: Input must be over 15 words"

def WrapText(submission, n):
    word_list = submission.split()
    op = []

    for i in range(len(word_list)):
        op.append(word_list.pop(0))
        if((i+1)%n==0):
            op.append("\n")
    #https://www.javaer101.com/en/article/38646746.html
    return "".join(x + " " if not "\n" in x else x for x in op)

# - Third, make each line begin with a capital letter, with all other letters 
# lowercase.
def CapitalizeLines(submission):
    lines = submission.split("\n")
    output = []
    for i in lines:
        original = i[0].upper()
        drop_first = i[1:].lower()
        output.append(original + drop_first)
    return "\n".join(output)

# - Return the resulting string. Display it with a print function, which should 
# show your line breaks at 5 words and the capitalization.
def FormatString(submission, n):
    ValidateString(submission)
    wrapped = WrapText(submission, n)
    return CapitalizeLines(wrapped)

user_input = "In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters."
words_per_line = 5

print(FormatString(user_input, words_per_line))

# Question 2 (50%): Pandas: Use the two small datasets included in the repo to 
# do the following:
# Load and merge the two dataframes on "msa". Explain in a 1-2 line comment
# which type of join is the appropriate one.

# Look at what happened to the "country", "year", and "month" columns after the
# merge. Redo the merge to fix the issue.

# Turn the "year" and "month" columns into a proper "date" column, with a 
# datetime datatype.

# Calculate a new column that shows the unemployment rate for each MSA.

# Oops! Something is clearly wrong with the Houston MSA. The correct labor
# force value is 2,733,348, but in reproducible research, we should never 
#directly modify the raw data, even when there are mistakes. Fix the value 
# using loc, then recalculate.

# Use the map method to make a new column that shows the unemployment rate
# formatted neatly as a percentage, with the % symbol after it. Note that you
# can do this other ways than with map, but for this question use map.

# Calculate the average unemployment rate for all of the MSAs. Now use loc to
# show only the subset of rows for which the unemployment rate is higher than
# the mean.

# Write the final dataframe to a new file named "data.csv" and commit it to
# your repo with your code. Since the dataframe index is not meaningful here,
# write it without the index.

# In[ ]:





# In[ ]:




