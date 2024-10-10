a = [int(v) for v in input().split()]
vmax=a[0];vmin=a[0]
for ing in a:
    vmax=max(ing,vmax)
    vmin=min(ing,vmin)
print(vmax,vmin)