if __name__ == '__main__':
    n = int(input())
    a = 1
    for i in range(2,n+1):
        if(i in range(0,10)):
            a = a*10 + i
        elif(i in range(10,100)):
            a = a*100 + i
        elif(i in range(100,1000)):
            a = a*1000 + i
        elif(i in range(1000, 10000)):
            a = a*10000 + i
        else:
            a = a*100000 + i
    print(a)
