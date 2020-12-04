def disemvowel(string):
    str = list(string)
    arr = []
    for i in str:
        if i not in list('aeiouAEIOU'):
            arr.append(i)
    print(''.join(arr))

disemvowel("what are you, a communist?")