#firstaprroch
def largest(num):
    return max(num)
def smallest(num):
    return min(num)
num= [34,44,5,3,5,3,2,455,32,4,555]
print(largest(num))
print(smallest(num))

#2nd approach not efficent

#def largest(num):
    #num.sort()
    #return num[-1]

#print(largest(num))

#3rd aprroach

def largest(num):
    largest = num[0]
    for x in num:
        if x > largest:
            largest=x
    return largest
num= [34,44,5,3,5,3,2,455,32,4,555]
print(largest(num))



