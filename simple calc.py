xy=input("enter the operations(+-*/)you want to perform:")
sum1=float(input("enter first no:"))
sum2=float(input("enter second no:"))

if xy=="+":
    result=sum1+sum2
    print(result)

elif xy=="-":
    result=sum1-sum2
    print(result)

elif xy=="*":
    result=sum1*sum2
    print(result)
    
elif xy=="/":
    result=sum1/sum2
    print(result)
else:
    print("invalid input")

