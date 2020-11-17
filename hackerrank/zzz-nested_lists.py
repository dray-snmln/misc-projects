"""
i kenat

from collections import OrderedDict 

student_marks = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_marks[name] = score

sort_by_marks = sorted(student_marks.items(), key=lambda x: x[1])
for x in sort_by_marks:
    while sort_by_marks[x] < sort_by_marks[x]:
        print(sort_by_marks[x])
"""