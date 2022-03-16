import pandas as pd

pd.set_option("precision", 2)

grades_dict = {'Wally':[87,96,70], 'Eva':[100,87,90], 'Sam':[94,77,90], 'Katie':[100,81,82], 'Bob':[83,65,85]}

#series = one dimensional array
#dataframe = two dimensional array where each column in DF is a series

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

eva = grades['Eva']

sam = grades.Sam

#using the loc and iloc methods

test2 = grades.loc['Test2']

test1 = grades.iloc[0]

#for consecutive rows need :

test1_thru_test3 = grades.loc['Test1':'Test3']

#for non consecutive rows need , and give a list

test1_and_test3 = grades.loc[['Test1', 'Test3']]

test1_and_test2 = grades.iloc[0:2]

#view only Eva's and Katie's grades for Test1 and Test2

E_and_K = grades.loc['Test1':'Test2', ['Eva', 'Katie']]

#view only Sam's thru bob's grades for Test1 and Test3

sam_thru_bob = grades.loc[['Test1', 'Test3'], 'Sam':'Bob']

#Boolean indexing

grades_A = grades[grades>=90]

#dataframe for everyone with B grade

grades_B = grades[(grades >=80) & (grades < 90)]

#grades A or B

grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]

#describe by student



print(grades.describe())

#by test

print(grades.T.describe())

#average of student grades on each test

print(grades.T.mean())

#sort rows by indices (test name)

r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column name
#axis = 1 sort by column indices
#axis = = sort by row indices

c_sorted_grades_i = grades.sort_index(axis=1)
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)




print()