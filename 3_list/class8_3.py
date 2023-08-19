#for loop with list and format
print("Example 1")
animals = ["lion","zebra","giraffe","dolphin","monkey"]
chars = 0
for animal in animals:
    chars = chars + len(animal)
print("Total characters: {}, Average length: {:.0f}".format(chars, chars/len(animal)))

print()
print("Example 2")
#enumerate
winners = ["Dhruv","Ankit","Falak"]
for index, person in enumerate(winners):
    print ("{} - {}".format(index+1, person))
    
print()
print("Example 3")
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("ghayaldhruv@example.com","Dhruv Ghayal"),("ankitpatel@example.com","Ankit Patel")]))
