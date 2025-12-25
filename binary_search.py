a=[1,5,12,14,18,19,25,27,36,37,45,49,52,58,78]
l=len(a)
t=int(input("Enter the require int: "))

low=0
high=l-1

while low<=high:
    mid=(low+high)//2

    if a[mid]==t:
        print("Element found at index", mid)
        break
    elif a[mid]>t:
        high=mid-1
    else:
        low=mid+1
else:
    print("No element found")




