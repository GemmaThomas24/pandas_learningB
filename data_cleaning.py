import pandas as pd
import numpy as np

# inconsistant, incomplete or inaccurate- called Dirty data
# Duplicates, typos, missing fields etc

# can impact all of results, the Mean and duplicates can skew stats
# data cleaning= filtering data you need, dropping unessary columns etc
# -----------------------------------------------
# Restructuring
# -----------------------------------------------
df = pd.read_excel("first_hour_sales.xlsx")
# print(df)

df = df.set_index("Transaction ID")

# print(df)
# --------------------------------------
# DROPPING
# --------------------------------------

df = df.drop(columns=["Till ID"])
df = df.drop(columns=["Staff ID"])

# print(df)

# .drop method can be used to remove rows as well- line 16-18 need removing 

df = df.drop([16,17, 18])

# print(df)

# .drop_duplicates()- auto search for a duplicate row and leaves 1 remaining 
df = df.drop_duplicates()

print(df)


# --------------------------------------
# OUTLIERS
# --------------------------------------
# points which sit abnoramlly far away from other values and can skew data
# True outliers are genuine data points- these should be left in (don't be in a rush to delete but it can impact data, especially a small collection of data)
# do assessmemnt of data with and without the outlier and compare


# print(df["Amount"].median())
# print(df["Amount"].mode())
# print(df["Amount"].mean())

# to change single cell, can use the .at property

df.at[12, "Amount"] = 3.10

# print(df)

# --------------------------------------
# Column Wide Cleaning
# --------------------------------------
# TIME column-
# for every float, turn into a string
# swap full stop for a :
# add a Zero at the start 00:00
# add 0 at end if need be

def float_to_time(stamp):
    stamp = str(stamp)
    stamp = stamp.replace(".", ":")
    stamp = "0" + stamp
    if len(stamp) !=5:
        stamp = stamp + "0"
    return stamp

def extract_time(stamp):
    stamp = stamp.time()
    return stamp

df["Time"] = df["Time"].apply(float_to_time)
# no () end of float to time- .apply will run function when needs to behind the scences- we're giveing ref to the function, not telling it to run right now
# line 69 only works as data is from 8- 9- won't work when go into double digits- which is why we applies the len(stamp)

df["Time"] = pd.to_datetime(df["Time"])
# .to_datetime is a Panda method- chnage the str format into actual date_time format
# print(df)

df["Time"] = df["Time"].apply(extract_time)
# This removes todays date that occurs when you run line 82

# print(df)

# print(df["Time"])

# --------------------------------------
# Prevention
# --------------------------------------
# free boxes not a good thing- others can put whatever they want the box
# Control Data- e.g drop down menus, tick boxes, casting, methods like .strip( and .capitalize()- will helo  clean the data)


# ------------------------------------------------------------------
# ACTIVITY 1
# ------------------------------------------------------------------
# Average price of an Item
# want to look at how many items sold and how much was made

# df["Average Price of Items"] = df["Amount"]/ df["Items"].sum()- incorrect
total_Items = df["Items"].sum()
total_amount = df["Amount"].sum()

print(total_amount/total_Items)
# want to assign the sum to the variables so we can do the working out

# Average Basket Price
# Transactions- what is the average price out of all the Transactions- Mean is the Average 

print(df["Amount"].mean())

# Maximum Spend in 1 Transaction
max_spend = df["Amount"].max()
print(max_spend)
# prints 56.5

# Minimun spen in 1 Transaction
min_spend = df["Amount"].min()
print(min_spend)
# prints 2.2

# Most common spend amount
most_common_amount = df["Amount"].mode()
print(most_common_amount)
# prints 2.85 and 3.10

# Most common Payment type
most_common_payment_type = df["Currency"].mode()

print(most_common_payment_type)
# print Debit