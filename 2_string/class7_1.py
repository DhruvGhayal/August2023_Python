#"{} {} ".format() method to combine string and number
name = "Dhruv Ghayal"
number = 9428244173
print ("Hello {}, your number is {}".format(name,number))

#EXAMPLE
def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#{:."number of digits after decimal point"f} formating method
price = 7.5
with_tax = price + price*(13/100)
print ("Base price:","$"+str(price)+","," After tax:","$"+str(with_tax))#Before formating  
print("Base price: ${:.1f}, After tax: ${:.1f}".format(price, with_tax))#After formating

#EXAMPLE
def to_celcius(f):
    c = ((f-32)*5)/9
    return c
for f in range ( 0, 101, 10):
    print("{:.1f}F | {:.3f}C".format(f, to_celcius(f)))#output 1

#EXAMPLE
#:>"max digit in the number is reccomanded" to space number 
def to_degree_celcius(f):
    c = ((f-32)*5)/9
    return c
for f in range ( 0, 101, 10):
    print("{:>3}F | {:>7.2f}C".format(f, to_degree_celcius(f)))#output 2
    
#Format with values in {}
first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)
"""Outputs:
apple carrot banana
"""