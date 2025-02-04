#** kwargs allows you to pass multiple keyword-arguments


#def print_address(**kwargs):
    #for key,value in kwargs.items():
        #print(f"{key} : {value}")


#print_address( apt="45d",street="123 fake st",city="detriot",state="mi", zip="123414")

#exc for both kwagrs and agrs

def shipping_label(*args, **kwargs):
    #for arg in args:
        #print(arg, end=" ")
    #print()

    #for kwarg in kwargs.values():
        #print(kwarg,end ="")
    if "apt"in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('zip')}")

    elif "popbox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('popbox')}")

    else:
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('apt')}")


shipping_label("dr","manoj","sqaurepants","iii",
               street="123 fake street",
               popbox="po box #1001",
               apt="100",
               city="detriot",
               state="mi",
               zip="123414")