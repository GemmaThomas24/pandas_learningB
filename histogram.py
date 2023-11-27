import matplotlib.pyplot as plt
import numpy as np

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32
        ]

plt.hist(dev_ages, edgecolor = "black", bins= [20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
plt.show()
# can specify bin size ourselfs


# print(len(dev_ages))- values 70
# dev_ages.sort()
# print(dev_ages[0])
# print(dev_ages[-1])
# 65-20= 45 = Range

# histogram- used for showing numerical data- similar to bar chart
# shows freq distributions- how often a value appears in an interval
# shows continuous data 
# each bar is a bin and groups data in ranges
# continuous data x axis and freq occurs y axis 
