#dictionary = a collection of {key:values} pairs ordered and changeable. no duplicates

capitals ={"usa": "washington dc",
           "india": "new delhi",
           "china":"beijing",
           "russia":"moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("usa"))
#print(capitals.get("india"))

if capitals.get("russia"):
    print("japan is in the dictionary")

else:
    print("japan doesnt exist")

#capitals.update({"usa":"detroit"})
#capitals.pop("china")
#capitals.popitem()
#capitals.clear()
#print(capitals)
keys= capitals.keys()
#print(keys)

#for key in capitals.keys():
    #print(key)

#values = capitals.values()
#print(values)   

#for value in capitals.values():
    #print(value)

items= capitals.items()
#print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")