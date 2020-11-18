s = input()
check = []
for _ in range(5):
    if s.isalnum() == True:
        check.append(1)
    elif s.isalpha() == True:
        check.append(1)
    elif s.isdigit() == True:
        check.append(1)
    elif s.islower() == True:
        check.append(1)
    elif s.isupper() == True:
        check.append(1)
    else:
        check.append(0)
for x in check:
    print(True if 1 else False)