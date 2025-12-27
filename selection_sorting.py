def sort(a):
    l=len(a)
    for i in range(l):
        min_index=i
        

        for j in range(i+1,l):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i ]

z=[12,45,23,52,62,71,3,63,27,1,13]
sort(z)
print(z)
