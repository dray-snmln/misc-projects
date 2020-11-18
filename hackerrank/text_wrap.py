def wrap(string, max_width):
    x = list(string)
    counter = 1
    for i in x:
        if counter % max_width != 0:
            print(i, end = '')
        else:
            print(i)
        counter += 1

string, max_width = input(), int(input())
result = wrap(string, max_width)