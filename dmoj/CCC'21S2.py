N = int(input())
M = int(input())
K = int(input())
rows = set()
cols = set()

# find rows and columns that will be changed
for i in range(K):
    opt, idx = input().split()
    idx = int(idx)-1
    if opt == 'R':
        if idx in rows:
            rows.remove(idx)
        else:
            rows.add(idx)
    else:
        if idx in cols:
            cols.remove(idx)
        else:
            cols.add(idx)

counter = 0
for i in range(N):
    for j in range(M):
        if (i in rows and j not in cols) or (j in cols and i not in rows):
            counter += 1

print(counter)