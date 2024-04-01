N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1
lnum = arr[left]
rnum = arr[right]

num = arr[left]+arr[right]
while(left<right):
    if(num==0):
        break
    elif(arr[left]+arr[right]<0):
        if(abs(num) > abs(arr[left]+arr[right])):
            num = arr[left]+arr[right]
            lnum = arr[left]
            rnum = arr[right]
        left+=1
    else:
        if(abs(num) > abs(arr[left]+arr[right])):
            num = arr[left]+arr[right]
            lnum = arr[left]
            rnum = arr[right]
        right-=1

print(str(lnum) + " " + str(rnum))