# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple key-value arguments
#         *unpacking operator
#      1.positional 2.deafult 3.keyword 4.arbitrary


#def add(*args):
    #print(type(args))
    #for arg in args:
        #total += arg
    #return total    

def display_name(*args):
    for arg in args:
        print( arg , end=" ") 

display_name("bob","code","vejv","everv") 

