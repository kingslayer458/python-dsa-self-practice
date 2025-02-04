item=input("what item do u want to buy:")
price=float(input("what is the price:"))
quantity=int(input("how many would u like:"))
total=price*quantity

print(f"you have bought {quantity} x {item}/s")
print(f"your total is :${total}")