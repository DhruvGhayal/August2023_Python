#TEST EXAMPLE
def NUMBER(number):
    if number > 11:print(0)
    elif number !=10: print(1)
    elif number >= 20 or number < 12 : print(2)
    else: print(3) 
NUMBER(10)

#TEST EXAMPLE WHOLE NUMBER LOGIC
def calculate_storage(filesize):
    block_size = 4096 
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks+1)
    return block_size * full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

#TEST EXAMPLE
# A function is created with the def() keyword. The parameter
# variable "time_as_string" is passed to the function through a 
# call to the function.
def task_reminder(time_as_string):
    # The following if-elif-else block assigns various strings to
    # the variable "task" depending on specific conditions. The
    # test conditions are set using the == equality comparison 
    # operator. In this case, the time passed through the 
    # "time_as_string" parameter variable is tested as the 
    # specific condition. So, if the time  is "11:30 a.m.", then 
    # "task" is assigned the value: "Run TPS report".
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    # The else statement is a catchall for all other values of 
    # the "time_as_string" parameter variable not listed in the
    # if-elif block of code.
    else:
        task = "Provide IT Support to employees"
    # This line returns the value of "task" to the function call.
    return task
# This line calls the function and passes a parameter  
# ("10:00 a.m.") to the function.
print(task_reminder("10:00 a.m."))
# Should print "Provide IT Support to employees"


#TEST EXAMPLE
# Example 1
# Evaluate the output of this print statement
def product(a, b):
        return(a*b)
print(product(product(2,4), product(3,5)))
#################################
# Example 2 
# Evaluate the output of this print statement
def difference(a, b):
        return(a-b)
def sum(a, b):
        return(a+b)
print(difference(sum(2,2), sum(3,3)))
#################################
# Example 3
# Evaluate the Boolean output of this comparison
print((5 >= 2*4) and (5 <= 4*3))
#################################
# Example 4 
# Evaluate the value of the comparison in the if statement 
x = 3
if x+5 > x**2 or x % 4 != 0:
        print("This comparison is True")
#################################
# Example 5 
# Evaluate the output of this if-elif-else statement
number = 6
if number * 2 < 14:
        print(number * 6 % 3)
elif number > 7:
        print(100 / number)
else:
        print(7 - number)
# Click Run to check your answers. If you are having trouble 
# calculating the correct answers manually, please review the
# Practice Quiz Study Guides, videos, and readings in this Module.