import numpy as np
import matplotlib.pyplot as plt

students = ["Arun", "Alice", "ann", "minnu", "elna"]
marks =  [70, 80, 90, 60, 50]

plt.plot(students, marks, marker='o')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("simple line plot")

plt.grid()
plt.show()
