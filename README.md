# Data Skills 2 - R
## Winter Quarter 2021

## Homework 4
## Due: Monday March 8th before midnight on GitHub Classroom


__Question 1 (50%):__ Python Skills Questions: As experts in R, you will need to develop your ability to look up the things you want to accomplish in Python while, wherever possible, leveraging what you already know about the relevant principles from R.

  1. The first day of class was January 11th, 2021.  Write code that shows how many days have elapsed between then and now, where "now" is the date someone runs your code. (Hint: look up the _datetime_ standard Python library.)
  2. Write code that begins with a Python list, containing some number of integers or floats. 
     * Multiply each value by 2. (Hint: look up *list comprehensions*)
     * Remove all odd numbers
     * Print a random value from the resulting list. (Hint: look up the _random_ standard Python library.)
  3. Write a Python **function** that takes a string as an argument, then returns a modified string.  Your function should:
     * First, test that the argument is a string, and that its length is at least 15 words. (Hint: look up the _assert_, _isinstance_, and _len_ standard Python functions, and the _split_ string method.)
     * Second, split the string into five or less words per line. (Hint: look up the _join_ string method.)
     * Third, make each line begin with a capital letter, with all other letters lowercase.
     * Return the resulting string.  Display it with a _print_ function, which should show your line breaks at 5 words and the capitalization.
    
__Question 2 (50%):__ Pandas: Use the two small datasets included in the repo to do the following:

  1. Load and merge the two dataframes on "msa".  Explain in a 1-2 line comment which type of join is the appropriate one.
  2. Look at what happened to the "country", "year", and "month" columns after the merge.  Redo the merge to fix the issue.
  3. Turn the "year" and "month" columns into a proper "date" column, with a datetime datatype.
  4. Calculate a new column that shows the unemployment rate for each MSA.
  5. Oops!  Something is clearly wrong with the Houston MSA.  The correct labor force value is 2,733,348, but in reproducible research, we should never directly modify the raw data, even when there are mistakes.  Fix the value using _loc_, then recalculate.
  6. Use the _map_ method to make a new column that shows the unemployment rate formatted neatly as a percentage, with the % symbol after it.  Note that you can do this other ways than with map, but for this question use map.
  7. Calculate the average unemployment rate for all of the MSAs.  Now use _loc_ to show only the subset of rows for which the unemployment rate is higher than the mean.
  8. Write the final dataframe to a new file named "data.csv" and commit it to your repo with your code.  Since the dataframe index is not meaningful here, write it without the index.

