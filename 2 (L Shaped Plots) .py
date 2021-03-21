for case in range(1,int(input())+1):
    h,w=map(int,input().split())
    plot=[list(map(int,input().split())) for i in range(h)]
    left=[[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if j==0:left[i][j]=plot[i][j]
            else:left[i][j]=(left[i][j-1]+1)*plot[i][j]
    right=[[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w-1,-1,-1):
            if j==w-1:right[i][j]=plot[i][j]
            else:right[i][j]=(right[i][j+1]+1)*plot[i][j]
    up=[[0]*w for i in range(h)]
    for i in range(w):
        for j in range(h):
            if j==0:up[j][i]=plot[j][i]
            else:up[j][i]=(up[j-1][i]+1)*plot[j][i]
    down=[[0]*w for i in range(h)]
    for i in range(w):
        for j in range(h-1,-1,-1):
            if j==h-1:down[j][i]=plot[j][i]
            else:down[j][i]=(down[j+1][i]+1)*plot[j][i]
    count=0
    for i in range(h):
        for j in range(w):
            u,d,l,r=[x[i][j] for x in [up,down,left,right]]
            count+=max(min(u-1,r//2-1),0)
            count+=max(min(u-1,l//2-1),0)
            count+=max(min(l-1,u//2-1),0)
            count+=max(min(l-1,d//2-1),0)
            count+=max(min(d-1,r//2-1),0)
            count+=max(min(d-1,l//2-1),0)
            count+=max(min(r-1,u//2-1),0)
            count+=max(min(r-1,d//2-1),0)
    print('Case #',case,': ',count,sep='')
            
