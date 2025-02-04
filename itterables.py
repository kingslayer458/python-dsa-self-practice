#itterables = an object/collection that can return its elements one at a time,
# allowing it to be iterated over in a loop

#list
number= [1,2,3,4,5]

for num in number:
    print(num, end=" ")
print()

#reversed

for num in reversed(number):
    print(num, end=" - ")
print()

#tuples

no = (1,2,3,4,5)

for n in no:
    print(n, end=" ")
print()


#sets
s = {1,2,3,4,5}

for se in s:#u cannot use reversed range fucntion in sets because its irreversible
    print(se, end="")
print()

#strings

name = "manoj kumar"

for ne in name:
    print(ne , end="-")
print("-------------------")
dict = {"rolno":"12","name":"manoj","grade":"best"}

print()
for key,value in dict.items():
    print(f"{key:10} {value:10} ")




