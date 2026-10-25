"""if is considered for all because all if are assessed,but all elif are 
not assessed."""

OS=input("Optional string: ")
alpha=0
digit=0
upper=0
lower=0
space=0
SC=0   #specific characters
for character in OS:
    if character.isalpha():
        alpha+=1
    if character.isdigit():
        digit+=1
    if character.isupper():
        upper+=1
    if character.islower():
        lower+=1
    if character.isspace():
        space+=1
    if character.isascii() and not character.isalpha()and not character.isdigit()\
        and not character.isupper()and not character.islower()\
        and not character.isspace():
        SC+=1
print("alpha=",alpha)
print("digit=",digit)
print("upper=",upper)
print("lower= ",lower)
print("space=",space)
print("SC= ",SC)
