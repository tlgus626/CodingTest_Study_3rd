n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

arr3=arr1+arr2
print(*sorted(arr3))
