n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
output = list((student_marks[query_name]))
# print(type(output))
per = sum(output)/len(output);
# per=1.234
print("%.2f" % per)
print("{0:.2f}".format(per))