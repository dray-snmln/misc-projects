def average(array):
    plants = set(array)
    return sum(plants) / len(plants)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)