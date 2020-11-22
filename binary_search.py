# Binary Search example logic. Use bisect.bisect if just arrays.
arr = [1, 2, 5, 8, 10, 23]
l = 0
r = len(arr)

x = 8

while l <= r:
    k = (l+r)//2
    if arr[k] == x:
        print(f'x found at {k}')
    if arr[k] > x:
        r = k-1
    else:
        l = k+1
