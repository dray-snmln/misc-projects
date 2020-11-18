s = input()
check = [0, 0, 0, 0, 0]
for a in s:
    if a.isalnum():
        check[0] += 1 
    if a.isalpha():
        check[1] += 1 
    if a.isdigit():
        check[2] += 1 
    if a.islower():
        check[3] += 1 
    if a.isupper():
        check[4] += 1 
for i in check:
    print(True) if i != 0 else print(False)