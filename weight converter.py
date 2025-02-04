w= float(input("enter your weight"))
unit= input("kilograms or pounds? (k or l):")

if unit == "L":
    w= w* 2.205
    unit = "lbs"

elif unit == "K":
    w= w/2.205
    unit ="kg"

else:
    print("invalid unit")

print(f"your final weight is {w} {unit}")    
