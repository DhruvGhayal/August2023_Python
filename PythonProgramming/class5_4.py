
# IF ELSE
def user_name(username):
    if len(username)<3:
        print("Invalid user name")
    else :
        print(username)
        
user_name("TODE")

def is_positive(number):
  if number > 0:
    return True
  else:
    return False
print(is_positive(-5))

def checkEven(number):
    if number% 2 == 0 :
        print("even number")
    else :
        print ("Odd number")
checkEven(3)

print("-----------------------------------")

#WITHOUT ELSE RETURN TRUE OR FALSE ONLY
def userName(user_name):
    if len(user_name)<3:
        print("Invalid user name")
    print(user_name)    
userName("Dhruv")

def is_positive_numb(number):
    if number > 0:
        return True
    return False
print(is_positive_numb(7))

#ELSEIF elif

def User_Name(xxx):
    if len(xxx) < 3: print(xxx,": Invalid user_name. User_Name should be > 3 char")
    elif len(xxx) > 7: print(xxx,":Invalid user_name. User_Name should be < 7 char")
    else : print(xxx,":Valid User_Name")

User_Name("Falak")