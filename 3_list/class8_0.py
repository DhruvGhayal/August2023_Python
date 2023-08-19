#LIST
x = ["Now","we","are","cooking"]
print(type(x))
print(x)
print(len(x))
print("today" in x)
print(x[2])
print(x[:3])

print("#############################################")
# append method
fruits = ["pinaple","mango","guava","banana"]
print("Total variety of fruits",str(len(fruits)))#before append(), there are 4 fruit
fruits.append("jackfruit")
print("After adding jackfruit")
print("Total variety of fruits",str(len(fruits)))#after append(), there are 5 fruit
print(fruits)
fruits.insert(2, "orange")
print("After adding orange")
print("Total variety of fruits",str(len(fruits)))#after insert(), there are 6 fruit
print(fruits)
fruits.remove("guava")
print("After removing guava")
print("Total variety of fruits",str(len(fruits)))#after insert(), there are 6 fruit
print(fruits)
