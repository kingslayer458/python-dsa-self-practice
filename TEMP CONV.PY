unit=input("is the temperature is celsius or farangeit(C OR F)")
temp=float(input("enter the temperature: "))

if unit =="C":
    temp= round((9*temp)/5 + 32,1)
    print(f"the temperature in fahrenheit is {temp}°F")

elif unit=="F":
    temp=round((5*(temp-32))/9,1)
    print(f"the temperature in celisius is {temp}C")

else:
    print("invalid")    