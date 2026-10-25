character=input("Password= ")
if character.isascii() and not character.isalpha()and not character.isdigit()\
and not character.isupper()and not character.islower()and not character.isspace():
    print("Password is valid.")
else:
    print("Password must contain at least 8 characters.") 
    print("Password must contain the specific character.")
    