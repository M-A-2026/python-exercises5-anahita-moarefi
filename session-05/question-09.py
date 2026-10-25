Attempts_Remaining=3
Attempts=[1,2,3]
for Numbers in Attempts:
    User=input("User: ")
    Password=input("Password: ")
    
    if len(User)>3 and User.isalpha() and\
    len(Password)>8 and Password.isascii()and not Password.isupper()\
    and not Password.islower() and not Password.isdigit():
        print("Login Successful") 
        break
        
    elif len(User)<3 or not User.isalpha() or \
         len(Password)<8 or not Password.isascii()or not Password.isupper()\
         or not Password.islower() or not Password.isdigit():
             Attempts_Remaining-=1
             print("Wrong Username or Password","Attempts Remaining=",Attempts_Remaining)
             
    elif len(User)<3 or not User.isalpha() or \
         len(Password)<8 or not Password.isascii()or not Password.isupper()\
             or not Password.islower() or not Password.isdigit():     
            print("Wrong Username or Password","Attempts Remaining=",Attempts_Remaining)     
           
    elif len(User)<3 or not User.isalpha() or \
         len(Password)<8 or not Password.isascii()or not Password.isupper()\
         or not Password.islower() or not Password.isdigit():
            print("Wrong Username or Password","Attempts Remaining=0",Attempts_Remaining) 
        