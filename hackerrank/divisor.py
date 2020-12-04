def divisors(integer):
    arr = []
    for i in range(1, integer):
        if integer % i == 0 and i != 1:
            arr.append(i)
    if len(arr) != 0:
        print(arr)
    else:
        print(f"{integer} is prime")
    
divisors(int(input()))