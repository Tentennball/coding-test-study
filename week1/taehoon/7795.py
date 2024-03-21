T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    arr1, arr2 = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())))
    ans = 0
    for i in range(A):
        left, right, = 0, B-1
        while(left<=right):
            mid = int((left+right) / 2)
            if(arr1[i]>arr2[mid]):
                left = mid + 1
            else:
                right = mid - 1
        ans+=left
    print(ans)