from heapq import*
import itertools

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

dirs=[(0,1),(1,0),(-1,0),(0,-1)]

def pprint(m):
    for i in m:print(*i)
    print()

for case in range(1,int(input())+1):
    h,w=map(int,input().split())
    l=[list(map(int,input().split())) for i in range(h)]
    b=[i[:] for i in l]

    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count
    found=0

    for i in range(h):
        for j in range(w):
            add_task((i,j),-l[i][j])

    while found<h*w:
        i,j=pop_task()
        for x,y in dirs:
            if 0<=i+x<h and 0<=j+y<w and b[i][j]>b[i+x][j+y]+1:
                b[i+x][j+y]=b[i][j]-1
                add_task((i+x,j+y),-b[i][j]+1)
        found+=1
        #print((i,j))
        #pprint(b)

    s=sum(b[i][j]-l[i][j] for i in range(h) for j in range(w))
    print('Case #',case,': ',s,sep='')
    #print(b)
