import random


#print(help(random), end="")
#print()

low= 1
high = 100
options = ("rock","paper","scissors")
cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

#number=  random.randint(low,high)
#number= random.random()#random no in floats
#print(number)
print(random.choice(options))
print(random.shuffle(cards))
print(cards)
