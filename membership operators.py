#memberhsip operators = used to test whether a value or variable is found in a sequence
#(string , list,tuple, set or dictionary)
#1. in
#2. not in


word= "apple"

#letter = input("guess a letter in the secret word:")


#in operator

#if letter in word:
    #print(f"there is a {letter}")
#else:
    #print(f"{letter} is not found")

#not in operator
#if letter not in word:
    #print(f"there is not{letter}")
#else:
    #print(f"there is a {letter}")

#another example
#sets
#students ={"manoj","karthik","sandy"}

#student =  input("enter the name of the student: ")

#if student in students:
   # print(f"{student} is a student")


#else:
    #print(f"{student} is not a student")

#if student not in students:
    #print(f"{student} is not a student")

#else:
    #print(f"{student} is a student")

#membership operators with dictionary
grades={"sandy":"A",
        "squidward":"B",
        "manoj":"C",
        "karthik":"D"}

#student = input("enter the name of the student: ")

#if student in grades:
    #print(f"{student} is a student and his grade is {grades[student]}")

#else:
    #print(f"{student} was not found")    


#if student not in grades:
    #print(f"{student} was not found")

#else:
   # print(f"{student} is a student and his grade is {grades[student]}")


email = "brocode@gmail.com"

if "@"in email and "." in email:
    print("this is a valid email")

else:
    print("this is not a valid email")