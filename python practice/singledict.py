create_dict={ "name":"manojkumar","Age":21,"Location":"Chennai"}

print(create_dict["name"])
print(create_dict["Age"])
print(create_dict["Location"])

#get method
print(create_dict.get("name"))#inside the get cannot be empty

#key method
print(create_dict.keys())

#values method
print(create_dict.values())

#in operator
for key in create_dict:
    print(key,create_dict[key])