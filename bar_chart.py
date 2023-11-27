import matplotlib.pyplot as plt
import numpy as np

advertising_locations =[
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
]

responses = [3,11,16,13,2]

# comparing different categories of data
# category typically x axis 
# categorical data is discrete data- can only be certain values, no middle ground.
# can highlight bar if necessary- called hero bar- if want to highlight certain thing
# best not to use colour in bar charts to avoid bias and show similarity 

bars = plt.bar(advertising_locations, responses)
bars[2].set_color("red")
plt.title("Return from Job Posting by Location")
plt.xlabel("Advert Location")
plt.ylabel("Applications received")

plt.show()

