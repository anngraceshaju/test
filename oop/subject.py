import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("subject.csv")
print(df)

plt.bar(df["Name"], df["average"])
plt.xlabel("Name")
plt.ylabel("average")
plt.title("student marks graph")

plt.show()

plt.bar(df["Name"], df["total"])
plt.xlabel("Name")
plt.ylabel("total")
plt.title("student marks graph")

plt.show()