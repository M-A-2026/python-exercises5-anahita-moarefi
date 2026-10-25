"""1.I define a sentence.
   2.BY split fun., I separate the words  into the sentence as list.
   3.The start of loop wrt split and count equals to 0.
   4.for loop includes word in words that are separated by split fun.
   5. Max Count is determined by count fun.based on the separated words.
   6.Now, we consider a condition, if MC is larger than count=0, print
   count based on MC and split based on word(number and name of max repititipn
                                             word are printed.)"""

S=input("Sentence= ")
words=S.split()
split=0
count=0
for word in words:
    MC=words.count(word)   #MC:max count
    if MC>count:
        count=MC
        split=word
print(split,count)
