creating_dictionary=[{"name":"manojkumar","rating":8.5, "experience":4},
{"name":"manoj","rating":8.5, "experience":4},
{"name":"manoj","rating":8.5333, "experience":4} ]
print(creating_dictionary)

for i in creating_dictionary:
    print(i)
#without using get method
result = creating_dictionary[0]["name"]
print(result)
print(creating_dictionary[2]["rating"])

#get method
value = creating_dictionary[0].get("name")
print(value)

value = creating_dictionary[2].get("rating")
print(value)

value = creating_dictionary[1].get("name")
print(value)