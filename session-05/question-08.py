Text=input("Text:")
Words=Text.split()
Character=0
Letter=0
word=0
Digit=0
Space=0
Upper=0
Lower=0
[ML,LW]=[0,0]    #Max Length and Longest Word
[ml,sw]=[0,0]    #min length and shortest word
[RC,L]=[0,0]
Count=0
RW=0
n=int(input("n="))
for Movement in Text:
    if Movement.isascii():    #space is included.
        Character+=1
    if Movement.isalpha():
        Letter+=1
    if Text.split():
        Word=len(Text.split())
        word+=1
    if Movement.isdigit():
        Digit+=1
    if Movement.isspace():
        Space+=1
    if Movement.isupper():
        Upper+=1
    if Movement.islower():
        Lower+=1    
    for Movement in Words:
        Length=len(Movement)
        if Length>ML and Movement.isalpha():
            ML=Length
            LW=Movement
        if Length<=ML-n and Movement.isalpha():
            ml=Length
            sw=Movement
    for char in Text:
        MRC=Text.count(char)
        if [MRC,char]>[RC,L] :           #Most Repeated Character  
            RC=MRC                       #RC:Count Repeated and L:Letter
            L=char
            print("MRC:",RC,"L:",L)
    for W in Words:
        MRW=Words.count(W)                #Most Repeated Word
        if MRW>Count:
            Count=MRW
            RW=W
            print("MRW:",Count,"NW:",RW)
            
print("Total Characters:",Character)
print("Total Letters:",Letter)
print("Total Words:",Word)
print("Total Digits:",Digit)
print("Total Space:",Space)
print("Total Uppper:",Upper)
print("Total Lower:",Lower)
print("Max Length:",ML,"Longest Word:",LW)
print("Min Length:",ml,"Shortest Word:",sw)
