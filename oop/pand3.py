import pandas as pd 
data = {
    "names":["anna", "nandhi", "ann", "sree", "ammu", "mittu", "elna", "deon"],
    "marks":[60, 80, 90, 70, 40, 50, 60, 20]
}

df=pd.DataFrame(data)
print(df.loc[0],df.loc[1])

