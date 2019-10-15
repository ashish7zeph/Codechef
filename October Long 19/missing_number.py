for _ in range(int(input())):
    n=int(input())
    ar=[[-1 for x in range(37)] for x in range(n)]
    for i in range(n):
        b,y=map(str,input().split())
        b=int(b)
        if b!=-1:
            ar[i][b]=int(y,b)
        else:
            for j in range(2,37):
                try:
                    ar[i][j]=int(y,j)
                except:
                    z=0
    o=[]
    for i in range(2,37):
        y=ar[0][i]
        cnt=0
        if y!=(-1) and y<=1000000000000:
            for j in range(1,n):
                if y in ar[j]:
                    cnt+=1
                else:
                    break
        if cnt==(n-1):
            o.append(ar[0][i])
    if len(o)>0:
        print(min(o))
    else:
        print('-1')
