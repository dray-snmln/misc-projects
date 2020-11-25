from itertools import combinations

x, y  = input().split()

for a in range(1, int(y)+1):
    for b in combinations(sorted(x), a):
        print(''.join(b))