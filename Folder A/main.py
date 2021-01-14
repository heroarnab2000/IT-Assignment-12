import series
while True:
    print()
    print("--MENU--")
    print("1. Division")
    print("2. Combination 1")
    print("3. 2's power")
    print("4. Combination 2")
    print("5. Exit")
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        a, b = map(int, input("Enter two numbers in the format (a/b): ").split('/'))
        print(series.division(a, b))

    elif ch == 2:
        a, b = map(int, input("Enter two numbers in the format (nCr): ").split('C'))
        print(series.nCr(a, b))
        
    elif ch == 3:
        a = int(input("Enter a number to find the range of 2's power: "))
        print(series.powerof2(a))
        
    elif ch == 4:
        a, b = map(int, input("Enter two numbers in the format (nCr): ").split('C'))
        print(series.B(a, b))
        
    elif ch == 5:
        print("Goodbye!")
        break
    else:
        print("Wrong input.\n")