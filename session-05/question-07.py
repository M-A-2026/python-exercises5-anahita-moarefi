""" The " ".join(dict.fromkeys(iterable)) function and variable.count(string) 
function are used to compress and count,respectively. To use count function, 
for loop must be used."""

string=input("string= ")
compress="".join(dict.fromkeys(string))
print("compress:",compress)
for letter in string:
    count=string.count(letter) 
    print(letter,count,end="  ")
