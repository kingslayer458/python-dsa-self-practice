create_dict=[{ "name":"manojkumar","Age":21,"Location":"Chennai"},
            { "name":"anuj kumar","Age":23,"Location":"chandigarh"},
            { "name":"rohan","Age":25,"Location":"pune"},
            { "name":"pavan","Agee":51,"Location":"mumbai"} ]

print(create_dict[0]["name"])
#print(create_dict["Age"])
#print(create_dict["Location"])
print("-----------------------")

#result = create_dict[2]["Age"]
#print(result)

#get funtion
#print(create_dict[1].get("name"))

#key method

print(create_dict[3].keys())

#values method
print(create_dict[2].values())
print(create_dict[1].values())

#in operator

for key in create_dict:
    print(key)