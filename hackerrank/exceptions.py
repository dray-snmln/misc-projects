arr = []
for i in range(int(input())):
    x, y = input().split()
    try:
        arr.append(int(x) // int(y))
    except ZeroDivisionError as e:
        arr.append(("Error Code: "+str(e)))
    except ValueError as e:
        arr.append(("Error Code: "+str(e)))
for i in arr:
    print(i)