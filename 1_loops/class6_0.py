#Loops
#EXAMPLE1
def num_ber(x):
    while x<5:
        print("not there yet,x =",str(x))
        x = x+1
    print("x="+str(x), "Loop ends!")
num_ber(0)

#EXAMPLE2
def userName(xxx):
    while len(xxx)<5:
        return ("Try Again!!")
        break
    return xxx
print(userName("Dhv"))

#EXAMPLE3
y=1
sum = 0
while y<10:
    sum += y
    y += 1
    
    product =1
    while y < 10:
        product = product * y
        y += 1
print(sum,product)

#EXAMPLE4
def count_down(current):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)

#EXAMPLE5
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n = n + 1
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 