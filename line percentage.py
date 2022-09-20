if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    # records = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # records.append()
    query_name = input()
    m=student_marks[query_name]
    s=0
    for i in m:
        s=s+i
    avg=s/3
    print("%.2f" % avg)