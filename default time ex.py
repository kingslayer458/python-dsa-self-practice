import time

def count(start, end):
    for x in range(start , end + 1):
        print(x)
        time.sleep(1)
    print("done")

count(0, 10)    