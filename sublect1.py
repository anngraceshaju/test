import matplotlib.pyplot as plt
#data
labels=['python', 'java', 'c++', 'javascript']
sizes=[40, 25, 20, 15]

#create pie chart
plt.pie(sizes, labels=labels)
plt.show()