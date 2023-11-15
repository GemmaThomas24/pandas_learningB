import pandas as pd
import numpy as np

df = pd.read_csv("cereal.csv")

# 1. How to show how many rows ans column are in the dataframe
print(df.shape)

# 2. How to show the name of the columns
print(df.columns)
# ! for ref there is 16 names

# 3. Which cereals have more than 4g of protein?
print(df.query('protein > 4'))
# was originally going to use something similar to this method: print(df.loc[0:3,"Languages": "Ranking 2020":2])
# was trying to research how to incorportate Int and finding cereal with more than 4g protein.
# found on google (stackoverflow) the .query method, wasn't sure if it would work. But when i tried it and checked it agaist the excel s/sheet it was right
# i thought it was more strightforward and easy to do.

# 4. print all data relating to Bran Flakes
print(df.loc[9, "name" :"rating":1])
# 9 is the index position of Bran Flakes row
# name is the start of the columns i need and rating is the end - [1] this makes sure it prints all the columsn as goes up by 1
