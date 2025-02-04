#keyword argument preceded by an indentifier helps with readability 

# order of agruments doesnt matter
# 1. posiyional 2. default 3.keyword 4.arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

#hello("hello", " mr", "spongebob", "sqaurepants")

#hello("hello", title="mr",last="sqarepants",first="manooj")

#for i in range(1,11):
    #print(i, end=" ")
print("1", "2","3","4","5","6", sep="-")