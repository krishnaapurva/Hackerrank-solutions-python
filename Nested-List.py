if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    student = sorted(student,key = lambda x:x[1])
    sec = (sorted(list(set(x[1] for x in student))))[1]
    des = []
    for st in student:
        if st[1]== sec:
            des.append(st[0])
    print('\n'.join(sorted(des)))    
