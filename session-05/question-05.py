"""I utilized List to show the inputs and to describe 
if(conditionalstatement) due to split function."""

String=input("String= ")
Words=String.split()
[LW,ML]=[0,0]          #Longest Word and Max Length   
for Word in Words:
    Length=len(Word)
    print(Word,Length)
    if[Length,Word]>[ML,LW] and Words.index(Word)<Words.index(Words):
        LW=Word
        ML=Length
print("Longest Word:",LW,";","Max Length:",ML)
