def solve(meal, tip, tax):
    x = meal * (tip / 100)
    y = meal * (tax / 100)
    total = meal + x + y
    print(round(total))

meal = float(input()) 
tip = int(input())
tax = int(input())
solve(meal, tip, tax)