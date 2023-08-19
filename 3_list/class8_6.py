### Simple List Comprehension
print("List comprehension result:")
# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)]) 
### Long form for loop
print("Long form code result:")
# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)
# Run to compare the two results.


### List Comprehension with Conditional Statement
print("List comprehension result:")
# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])
### Long form for loop with nested if-statement
print("Long form code result:")
# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)
# Run to observe the two results.


#PRACTICE EXAMPLE
def squares(start, end):
    return [n**2 for n in range(start, end+1)]
print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]