Text=input("Text= ")
Words=["hack","fraud","scam","password","attack"]
print("Output")
for Word in Words:
    if Text.count(Word):
        print(Word,">>>>>>",Text.count(Word))
        