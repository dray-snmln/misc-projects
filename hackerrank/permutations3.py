from itertools import combinations_with_replacement

x, y = input().split()
for i in combinations_with_replacement(sorted(x), int(y)):
    print(''.join(i))