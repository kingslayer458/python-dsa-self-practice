# while loop = execute some code while some conditon remains true

#name = input("enter your name:")

#while name == "":
    #print("you did not enter your name")
    #name = input("enter your name:")

#else:
    #print(f"hello{name}")    


food = input("emter your favorite food(press q to quit:)")

while True:
    print(f"you like{food}")
    food = input("enter your another favorite food(press q to quit:)")
    if food == "q":
        break