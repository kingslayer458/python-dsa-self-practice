#variable scope = where a vraiable is visible and accessible
# scope resolution =(LEGB) local  -> Enclosed -> Global -> built in

def func1():
    a= 1
    print(a)

def func2():
    b =1
    print(b)

func1()
func2()