#LIST COMPREHENSIONS
#Skill 1
print("Without list comprehensions")
multiple = []
for x in range (1,11):
    multiple.append(x*7)

print(multiple)

print("With list comprehensions")
multiples = [ x * 7 for x in range (1,11) ]
print(multiples)

#CLASS EXAMPLE
lang = ["python","perl","ruby","go","java","C"]
#JAVA LOGIC
#l = len(lang)
#print(l)
#for i in range(0,l):
#    print(i+1,lang[i],len(lang[i]))
    
#PYTHON LOGIC
#SKILL 2
languages = ["python","perl","ruby","go","java","C"]
lengths = [len(language) for  language in languages]
print(lengths)

#CLASS EXAMPLE
xx = []
#for divisible in range(0,101):
    #if divisible%3 == 0:
     #   print(divisible)
divisible = [z for z in range (0,101) if z%3 == 0]
print (divisible) 
