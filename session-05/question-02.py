"""The dict.fromkeys() function is related to dictionary not string.Hence,I
used the join function (a type of string function) that the input of it
 can be iterable.In addition, the empty double quotation is used as replace."""
 
string=input("Optional string=")
result="".join(dict.fromkeys(string))
print(result)
