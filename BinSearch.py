# Binary Search code. Use bisect.bisect if just arrays.
arr=[1,2,5,8,10,23]
a=0
b=len(arr)

x = 8

while a<=b:
    k = (a+b)//2
    if arr[k] == x:
        print(f'x found at {k}')
    if arr[k] > x: b=k-1
    else:          a=k+1

