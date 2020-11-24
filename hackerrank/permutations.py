from itertools import permutations

x, y = input().split()
xlist = permutations(list(x), int(y))
for i in sorted(xlist):
    print(''.join(i))