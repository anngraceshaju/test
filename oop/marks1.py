import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("oop/marks.csv")
print(df)

plt.scatter(df["Name"], df["Marks"])
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student marks graph")

plt.show()

