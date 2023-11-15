import pandas as pd
import numpy as np

# Pandas allow us to create single-dimentional arrays called Panda Series = like a list
# Pandas Series(Series is a Class) -is like a column in a table and stores data of the same subject
# languages object has been made below. Stores different types of languages. Series Object- has all the properties of series object
# Dtype- strings/mixed info in a series prints as an object
languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

print(languages)

ranking = pd.Series([3,1,2,4])

# print(ranking)

# these are the positions of these langauges in the Stack Overflow Developer Survey.
# int64 - integer only allow to be within a range of num that exists. 64 bit int has a max limit allowed and a lower limit. Shouldn't be bigger than 64 bits wide.
# 2 to the power of 63 - 1 - (over 9 quintillion) in range of positive to negative.

# Series only a column- 1D
# Data Frame = The variable storing the dataframe is called df. It's looks like an excel s/sheet with muliple columns
# we create new DF using Class Dataframe
# Pandas groups data based on index postion 
# need to look into kwarg again***

# df = pd.DataFrame([("Anne", 30),("Bill", 27),("Charlie", 55)], columns = ["Name", "Age"])

# print(df)

# Making dataframe from from existing series we created above- useing dictionary. Key = Column Name and Value Series (the list of data)
df = pd.DataFrame({
    'Languages' : languages,
    'Ranking' : ranking
})

# print(df)

# pd.concat() method which works in panda library(before would use + in python)- want to join 2 list
# axis = 1 - telling it what axis the Series should be joined at. puts them next to eachother in columns
# axis - 0 stack on top of eachother- ROWS
# can use this structure or dictionary way- both widely used to merge 2 dataframes or series

# ------------------------------------------------------------------------------------------------------
#                         AMENDING DATA STRUCTURES
# ------------------------------------------------------------------------------------------------------

# .loc = location

df.loc[4] = ["PHP", 11]
# print(df)
# amending location property of the DF. [] is the index postion of the rows. = assign to that index positon [PHP and 11]- 
# PHP is index postion 0 and 11 is 1, this will be added to the dataframe as such under the columns we created

# .concat Method
new_data = pd.DataFrame({"Languages": ["PHP"], "Ranking": [11]})
df = pd.concat([df, new_data], ignore_index=True)
# can only concat series to series/frame to frame.
# above we already have DataFrame Dictionary that includes Lang and Ranking.
# to add the new data to this DF, we create a new_data variable.
# assign 'PHP' to Languages column and assign 11 to Ranking column
# underneath we concatinate [df and new_data]- amd ignore the index to make it look coherant.

df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]
# print(df)


df["Ranking 2022"] = [4,1,2,3,10,6,5]
# print(df)
# there's 7 rows- need to input 7 bits of data or there will be an error
df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]

# print(df)

# how to add columns in a specific position- see below
# .insert() method, add cloumn at a index postion- 3 parameters

df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])

print(df)
# print(df.columns)- brings up columns names
# how to find out index posion of coloumns if we have too many?? see line 84
# df.columns.get_loc("ranking 2022")


# how to input row as specific postion- 
# df.loc[3.5](this will put between index postion 3 and 4) = ["language random", 10, 45, 2,4,6]
# df = df.sort_index()- will change index position to floating point and chnage from 1 to 1.0.

# ----------------------------------------------------------------------------------------------
#                             ACCESSING DATA STRUCTURE
# ----------------------------------------------------------------------------------------------

# TO SEE HOW BIG DF IS- CAN ACCESS THE.SHAPE PROPERTY - retunr size of DF in rows and columns
# 
# print(df.shape)
# 7 rows, 6 columns- 7x6 = 42 values to work with in the DF.

# print(df.columns)- names of the columns 
# access data within the DF. use Square Brackets
# e.g- print (df["Ranking 2019"])- returns that one column and the data - []- double the square brackets to see what list of columns you want to see
# print(df[["Ranking 2019", "Ranking 2020"]])

print(df.loc[4])

print(df.loc[:, "Ranking 2020"])

# .loc expects info in certain way: df.loc[start:stop:step, start:stop:step]
#                                             row                column

# (df.loc[4:7, "Ranking 2020"])- row 4 to row 7 

print(df.loc[0:3,"Languages": "Ranking 2020":2])
# 2 shows every other column
# 0:3 rows 0-3 (commer) "Languages (start): "Ranking 2020" (Stop here): 2 (only show every 2 columns)

# selecting data based on a conditon:
# < comparison operator. Creates a boolean data type Yes or NO
# print(df[df<4])
# print(df[df.index<4])
# can't compare Int 4 to String(coming from 1st column which is only strings - name of lang)
# need to narrow down the search to just the int in our frame
# method is .select_dtypes()

# print(df[df.select_dtypes(include="int") < 4 ])
# Nan means not a number- what is FALSE will show as nan



