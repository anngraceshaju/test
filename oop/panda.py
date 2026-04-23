import pandas 
mydataset ={
    "cars": ["BMW", "VOLVO", "FORD"],
    "passengers":[3,7,2]
}

mycar = pandas.DataFrame(mydataset)

print(mycar)