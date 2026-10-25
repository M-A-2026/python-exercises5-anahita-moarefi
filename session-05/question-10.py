Sentence1=input("Sentence1:")
Sentence2=input("Sentence2:")
Sentence=Sentence1+" "+Sentence2
print(Sentence)
Words=Sentence.split()
print(Words)
count=0
Word=0
for Word in Words:
    if Words.count(Word)>1:
        MC=Words.count(Word)
        MC>count
        Word=Word
        print("Max Count:",MC,"Word:",Word)
          