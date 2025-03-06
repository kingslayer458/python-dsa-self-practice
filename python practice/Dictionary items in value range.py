d = {'a':10,'b':23, "c":45,"d":90}
print(d)

res = {}

for key, val in d.items():

    if 45 <= val :
        res[key] = val

print(res)       