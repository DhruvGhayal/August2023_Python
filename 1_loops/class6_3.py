#For loop
for x in range (5):print (x)
print("##############################")
#ranging For loop to print 1 to 5
for y in range (1, 6): print (y)
print("##############################")
#another method
for z in range (1, 5+1): print (z)
print("##############################")
#EXAMPLE 
product = 1
for n in range (1,10): 
    print (product)
    product = product * n
print("##############################")
#EXAMPLE for loop with range and value increment 
#convert F to C
def to_celcius(f):
    c = ((f-32)*5)/9
    return c
for f in range ( 0, 101, 10):
    print(f, to_celcius(f))
    