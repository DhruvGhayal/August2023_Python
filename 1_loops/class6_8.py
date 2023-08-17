'''
print("TEST EXAMPLE 1")
number = 2 # Initialize the variable 
while number <= 12 : # Complete the while loop condition
    print(number, end=" ")
    number += 2 # Increment the variable
# Should print 2 4 6 8 10 12 
print()
print("TEST EXAMPLE 2")
for n in range (5, -1, -1):
    print(n)

print()
print("TEST EXAMPLE 3")
def factorial(n):
    result = n
    start = n
    n -= 1
    while n>0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1  # Decrement the appropriate variable by -1
    return result

print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

print()
print("TEST EXAMPLE 4")
def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(1, 3+1): 
         # Complete the inner loop range
        for y in range(1, 3+1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()
multiplication_table(1, 3)
# Should print the multiplication table shown above'''

print()
print("TEST EXAMPLE 5")
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start > stop:
            return_string += str(start)+","
            start -= 1
    else:
        return_string = "Counting up: "
        while start < stop:
            return_string += str(start)+","
            start += 1
    return_string += str(stop)
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"