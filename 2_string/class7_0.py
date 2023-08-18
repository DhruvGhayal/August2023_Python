#string length, print character, character range
name = "Dhruv you are the best"
print(name[2]) #print character at D h r = 0 1 2
print(len(name))#including space
print(name[-1])#print character at D h r u v = -5 -4 -3 -2 -1
print(name[5:13])#print range of character
fruit = "Mangosteen"
print(fruit[:5])
print(fruit[5:])
print(fruit[:5] + fruit[5:])

#knowing string index
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("D"))

#know if string contains certain char or not
print("dogs" in pets)
print("Cats" in pets)

#EXAMPLE
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("ghayal.dhruv.87@yahoo.com", "yahoo.com", "gmail.com"))

#Different methods used in string
#Upper lower strip lstrip rstrip count("_") isnumeric join endswith("_")
print("dhruv".upper())
print("DHRUV".lower())
print(" D H R U V ".strip())#remove space from both sides
print(" D H R U V ".lstrip())#remave space from left side
print(" D H R U V ".rstrip())#remove space from rightside
print("this number of times e occur in string eeee".count("e"))
print("1 2 3 4 5".isnumeric())
print("12345".isnumeric())
print(int("12345")+int("54321"))
print("...".join(["This","is","a","phrase","joined","by","dots"]))
print("this sentence is splitted and all the words are listed by split".split())