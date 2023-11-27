import matplotlib.pyplot as plt
import numpy as np

# years = [2018, 2019, 2020, 2021, 2022, 2023]

# python_position = [7, 4, 4, 3, 4, 3]

# javascript_positon = [1, 1, 1, 1, 1, 1]

# sql_position = [4, 3, 3, 4, 3, 4]

# typescript_position = [12, 10, 9, 7, 5, 5]

# plt.plot(years, python_position)
# # adding more data sets to compare 
# plt.plot(years, javascript_positon, linestyle = "dashed")

# plt.plot(years, sql_position, linestyle = "dotted")

# plt.plot(years, typescript_position, linestyle ="dashdot")

# # assign main title to the Plot
# plt.title("Most Popular Language - Ranking")

# # xlabel()and ylabel()- methods allow us to label axis 
# plt.xlabel("Year")
# plt.ylabel("Ranking Position")

# # ylim()method- allows us to set the limits of the y-axis 
# plt.ylim(bottom = 12, top = 0)

# # lengends used to describe data on a chart- to make reference point/Key. Have to put in order wrote the code.
# plt.legend([
#     "Python",
#     "JavaScript",
#     "SQL",
#     "TypeScript"
# ])
# # not sustainable on how to create a Key. Can use label to assign name to line of data when 1st make it a plot
# # plt.plot(years, python_position, label = "Python")
# # then can use .legend and it will take from that info, don't have to remember order.
# # can customise formatting of plot, but beware of over-formatting

# # 1 reason of formatting- accessability
# # line styles- help differentiate between data- linestyle argument
# # plt.plot(years, typescript_position, label = "python", linestyle = "dashed")

# plt.show()

# ------------------------------------------------------------------------------------
# CHALLENGE 1
# ------------------------------------------------------------------------------------

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

youtube = [2, 1, 3, 6, 3]

twitter = [1, 1, 0, 0, 2]

whatsapp = [3, 1, 0, 2, 1]

raid_shadowlegends = [0, 4, 2, 3, 3]

tiktok = [3, 0, 1, 0, 2]

plt.plot(days_of_week, youtube, label = "Youtube", marker = "o", color = "r")
plt.plot(days_of_week, twitter, label = "Twitter", linestyle = "dashed", marker = "s", color = "c")
plt.plot(days_of_week, whatsapp, label = "Whatsapp", linestyle = "dotted", marker = "P", color = "g")
plt.plot(days_of_week, raid_shadowlegends, label = "Raid:Shadow Legends", linestyle = "dashdot", marker = "x", color ="m")
plt.plot(days_of_week, tiktok, label = "TikTok", linestyle = (0, (5, 10)), marker = "*", color = "k")
# loosley dashed


plt.title("Weekly Screen-Time")
plt.xlabel("Days of Week")
plt.ylabel("Hours per day")
plt.ylim(bottom = -1, top = 10)
plt.legend()

plt.show()

# ------------------------------------------------------------------------------------
# CHALLENGE 2
# ------------------------------------------------------------------------------------
# adding Markers- see above for markers added in line 66 to 70
# changing colours of the lines - see line 66 to 70