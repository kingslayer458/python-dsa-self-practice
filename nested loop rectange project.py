rows = int(input("enter the no of rows: "))
columns = int(input("enter the no of columns: "))
symbol = (input("enter the no of symbol to use: "))





for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()