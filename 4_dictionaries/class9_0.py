#Dictionaries
x = {}
print(type(x))

#dictionaries are same as MAPS in JAVA they take values like key:value
file_count = {"jpeg":10, "txt":14, "csv":2, "py":23}
print(file_count)
print("jpg" in file_count)
print("csv" in file_count)
#add to dictionary
file_count["png"]=15
print(file_count)
file_count["csv"] = 17
print(file_count)
#delet from dictionary
del file_count["csv"]
print(file_count)

# items() keys() values()
print(file_count.items())    
print(file_count.keys())
print(file_count.values())

# drctionary tuples
file_count = {"jpeg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_count.items():
    print ("{} has {} files".format(ext, amount))