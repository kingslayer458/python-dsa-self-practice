#list comprehension =  a concise way to create lists in  python
#      compact and easier to read than traditonal loops
#[expression for value in iterable if condtion]


#doubles = []

#for x in range(1,11):
    #doubles.append(x*2)
#print(doubles)


#doubles = [ expression for x in range(1,11)]

#doubles = [ x * 2 for x in range(1,11)]
#triple = [ x * 3 for x in range(1,11)]
#square = [ z * z for z in range(1,11)]
#print(doubles)
#print(triple)  
#print(square)


#strings


fruits = ["apple","orange","banana","coconut"]

#fruits = [ fruit.upper() for fruit in fruits]

#fruits = [ fruit for fruit in fruits]
#print(fruits)

numbers = [1, -2, 3, -4, 5, -6]

#positive_nums=[num for num in numbers if num >=0]
#negative_nums=[num for num in numbers if num <=0]
#even_nums=[num for num in numbers if num %2 ==0]
#odd_nums=[num for num in numbers if num %2 ==1]
#print(positive_nums)
#print(negative_nums)
#print(even_nums)
#print(odd_nums)

grades = [85,42,79,90,56,61,30]
passing_grades=[grade for grade in grades if grade >= 60]

print(passing_grades)

