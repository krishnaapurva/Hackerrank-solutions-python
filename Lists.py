if __name__ == '__main__':
    N = int(input())
    li = []
    for _ in range(N):
        opr , *vr = input().split()
        sc = list(map(int,vr))
        if (opr == 'insert'):
            li.insert(sc[0],sc[1])
        elif( opr == 'print'):
            print(li)
        elif(opr == 'remove'):
            li.remove(sc[0])
        elif(opr == 'append'):
            li.append(sc[0])
        elif(opr == 'pop'):
            li.pop()
        elif(opr == 'sort'):
            li.sort()
        elif(opr == 'reverse'):
            li.reverse()
