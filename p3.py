n, k = map(int, input().split())
a = [int(v) for v in input().split()]

a.sort()

print("Day tang dan la: ", *a)

curx= 1
cnt = []
for i in range(1, n):
    if a[i]==a[i-1]: 
        curx+=1
        if(curx==k): cnt.append(a[i])
    else: curx = 1

print(f"Cac so xuat hien {k} lan tro len la: ", *cnt)