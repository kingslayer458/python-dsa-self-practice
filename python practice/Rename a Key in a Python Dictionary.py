data ={"manoj":4,"ankush":5,"pavan":6}
print(data)

print("initial dictionary",data)
data["rohan"] = data["ankush"]
del data["ankush"]

print("final dictiionary",str(data))