#for loops =  execute a block of code a fixed number of times
# you can iterate over a range ,string, sequence, etc


#range
#for x in reversed(range(1,11)):
    #print(x)
#print("HAPPY NEW YEAR")

#for x in (range(1,11)):
    #print(x)
#print("HAPPY NEW YEAR")

#for loop using step

#for i in range(1,11,2):
    #print(i)

#string

#credit_card  ="1234-5678-9012-3456"

#for x in credit_card:
    #print(x)

#to skip a iteration use continue kyeword
#continue used to skip the int

#for x in range(1,21):
    #if x == 13:
        #continue
    #else:
        #print(x)
for x in range(1,21):
    if x==13:
        break
    else:
        print(x)

