for case in range(1,int(input())+1):
    n=int(input())
    m=[list(map(int,input().split())) for i in range(n)]
    c=[list(map(int,input().split())) for i in range(n)]
    input()
    input()
    edges=[]
    for i in range(n):
        for j in range(n):
            if m[i][j]==-1:
                edges.append((c[i][j],~i,j))
    edges.sort()

    d={i:{'head':i,'depth':0} for i in range(-n,n)}

    price=0
    for cost,a,b in edges[::-1]:      
        while d[a]['head']!=a:
            d[a]['head']=d[d[a]['head']]['head']
            a=d[a]['head']
        while d[b]['head']!=b:
            d[b]['head']=d[d[b]['head']]['head']
            b=d[b]['head']
        if a==b:
            price+=cost
        else:
            if d[a]['depth']>d[b]['depth']:
                d[b]['head']=a
            else:
                d[a]['head']=b
                d[b]['depth']=max(d[b]['depth'],d[a]['depth']+1)

    print('Case #',case,': ',price,sep='')
        
