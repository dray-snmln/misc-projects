def closest_higher_mod_5(x):
    while x % 5 != 0:
        x += 1
    print(x)

closest_higher_mod_5(int(input()))