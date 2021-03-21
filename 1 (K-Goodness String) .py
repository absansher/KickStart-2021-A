def good(s):
    t=0
    for i in range(1,len(s)//2+1):
        if s[i-1]!=s[len(s)-i]:
            t+=1
    return t

for case in range(1,int(input())+1):
    x,y=map(int,input().split())
    s=good(input())
    print('Case #',case,': ',abs(s-y),sep='')
    
