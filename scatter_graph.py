import matplotlib.pyplot as plt
import numpy as np

number_of_placements= np.array(range(1,11))
responses_received = np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])

plt.scatter(number_of_placements, responses_received)
plt.title("Job Posting- Junior Dev Role")
plt.xlabel("Number of Place Advertised")
plt.ylabel("Responses Received")

m,c = np.polyfit(number_of_placements, responses_received, 1)
# finds M and C
plt.plot(number_of_placements, m*number_of_placements+c)
# x, m times x(num of placements)+ C = gives Y

plt.show()

# scatter graph- to show correlation between the independant and dependant variable
# line of best fit- give best approximation oft he data- from it we can make small
# predictions and visulaise a relationship easier.
# array- need to amend data to include this to make line of best fit
# array- like a list but stricter
# line of best fit is a form of regression. Regression is the process of estimating relationship
# between variables