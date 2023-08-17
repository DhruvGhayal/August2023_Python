#PRACTICE EXAMPLE 1
print(32 == 30+2)   # The == operator checks if the 2 values are 
#True                # equal to each other. If they are equal, 
                    # Python returns a True result.
print(5+10 == 6+7)  # If the two values are not equal, as in the
#False               # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.
print(10-4 != 10+4) # The != operator checks if the 2 values are
#True                # NOT equal to each other. If true, Python              
                    # returns a True result. 
print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
#False               # is false. So, Python returns a False value.

#PRACTICE EXAMPLE 2
# The = equals assignment operator is used to assign a value to a 
# variable.
my_variable = 3*5           # Assigns a value to my_variable      
print(my_variable)          # Printing the variable returns the 
#15                          # value assigned to the variable.                   
# The == equality comparison operator checks if the values of the two
# expressions on either side of the == operator are equivalent to one 
# another.
print(my_variable == 3*5)   # Printing the variable returns a Boolean 
#True                        # True or False result. 

#PRACTICE EXAMPLE 3
print(11 > 3*3)         # The > operator checks if the left value is
#True                    # greater than the right value. If true, it
                        # returns a True result.
print(4/2 > 8-4)        # If the > operator finds that the left value
#False                   # is NOT greater than the right value, the
                        # comparison will return a False result.
print(4/2 < 8-4)        # The < operator checks  if the left value is
#True                    # less than the right side. If true, the
                        # comparison returns a True result.
print(11 < 3*3)         # If the < operator finds that the left side is False                   
                        # NOT less than the right value, Python returns
#False                   # a False result.

#PRACTICE EXAMPLE 4
print(12*2 >= 24)   # The >= operator checks if the left value is
#True                # greater than or equal to the right value. 
                    # If one of these conditions is true,  
                    # Python returns a True result. In this case  
                    # the two values are equal. So, the comparison
                    # returns a True result.
print(18/2 >= 15)   # If the >= comparison determines that the left False
#False               # value is NOT greater than or equal to the
                    # right, it returns a False result.
print(12*2 <= 30)   # The <= operator checks if the left value is
#True                # less than or equal to the right value. In 
                    # this case, the left value is less than the
                    # right value. Again, if one of the two 
                    # conditions is true, Python returns a True
                    # result.
print(15 <= 18/2)   # If the <= comparison determines that the left 
#False               # value is NOT less than or equal to the right
                    # value, the comparison returns a False result. 
                    
                    
                    
                    
                    
''' 
         Python comparison operators return Boolean results: True or False.

Symbol    Name                                 Expression      Description

==        Equality operator                     a == b          a is equal to b

!=        Not equal to operator                 a != b          a is not equal to b

>         Greater than operator                 a > b           a is larger than b

>=        Greater than or equal to operator     a >= b          a is larger than or equal to b

<         Less than operator                    a < b           a is smaller than b

<=        Less than or equal to operator        a <= b          a is smaller than or equal to b
'''