#fruits = ["apple", "orange", "banana","coconut"]
#vegetables = ["celery","carrots","potatoes"]
#meats = ["chicken","fish","turkey"]


#another way to represent

groceries = [["apple", "orange", "banana","coconut"], 
             ["celery","carrots","potatoes"],
             ["chicken","fish","turkey"]]


#print(groceries[1][2])
#print(groceries[0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")  # prints each food item in the list of lists
    print()    