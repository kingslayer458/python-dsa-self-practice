data ={"manoj":4,"ankush":5,"pavan":6}
print(data)

print("initial dictionary",data)
#data["rahul"] = data.pop("manoj")

#print("final dictionary", str(data))#str is not compulsory it automatically converts dict to strings
#ini_list = ['a', 'b', 'c', 'd']

#using zip function
#data = dict(zip(ini_list, list(data.values())))
#print(data)

#.items() is used to get both keys and values
# .keys() is used to get keys
# .values() is used to get values
new_data={}
for key,value in data.items():
    if key == "manoj":
        new_data["apple"] = value
    else:
        new_data[key] = value
del data
print(new_data)
