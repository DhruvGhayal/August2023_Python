#FUNCTIONS
#def keyword is used to define function
def greeting (name):
    print("Welcome " + name)

greeting("Dhruv")

def Greeting(name, department):
    print("Welcome " + name)
    print("You are " +department)
    
Greeting("Dhruv", "QA Automation Engineer")

#PRACTICE EXAMPLE
def triangle_area(base, altitute):
    return ((base * altitute)/2)

area_A = triangle_area(5, 4)
print(area_A)
area_B = triangle_area(7, 3)
print(area_B)
sum_of_triangle_area = area_A + area_B
print ("The sum of two triangle area is equal to " + str(sum_of_triangle_area))

# // for quotien and def
print(5/2)#division
print(5//2)#module
# convert seconds to hh mm ss formate example
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = ( seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
print(convert_seconds(3686))

#String length using len
name = "Dhruv"
print(len(name))

#EXAMPLE
def area_of_circle(r):
    pi = 3.141592653589793238462643383279502884197
    return (pi * (r**2))

print(area_of_circle(5))
    
    