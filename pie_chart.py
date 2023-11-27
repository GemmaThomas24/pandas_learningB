import matplotlib.pyplot as plt
import numpy as np

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

plt.pie(employees, labels=roles, autopct= "%.2f%%",
        explode=[0.2, 0, 0, 0])
# 0.2 = moves away from center
# 0 = stays in the centre
plt.title("Developer Roles")
#quickly and clearly show how parts of data make a whole result
# works best with a handful of data 

plt.savefig("pie.png")

plt.show()

# make sure plt.save, before plt.show or it will wipe