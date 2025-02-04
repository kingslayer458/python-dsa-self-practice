# format specifiers = {value:flags} format a value based on what falgs are inserted


price1 = 3.14159
price2 = -987.6531
price3 = 12.34313

#print(f"price 1 is {price1:.1f}")
#print(f"price 2 is {price2:.1f}")
#print(f"price 3 is {price3:.1f}")

#giving spaces
#print(f"price 1 is {price1:10}")
#print(f"price 2 is {price2:10}")
#print(f"price 3 is {price3:10}")

#giving zero padded
#print(f"price 1 is {price1:010}")
#print(f"price 2 is {price2:010}")
#print(f"price 3 is {price3:010}")

#center align
#print(f"price 1 is {price1:^}")
#print(f"price 2 is {price2:^}")
#print(f"price 3 is {price3:^}")


#right align

#print(f"price 1 is {price1:>}")
#print(f"price 2 is {price2:>}")
#print(f"price 3 is {price3:>}")


#left align

#print(f"price 1 is {price1:<}")
#print(f"price 2 is {price2:<}")
#print(f"price 3 is {price3:<}")


print(f"price 1 is {price1:+,.2f}")
print(f"price 2 is {price2:+,.2f}")
print(f"price 3 is {price3:+,.2f}")