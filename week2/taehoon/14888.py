import sys
N = int(input())
arr = list(map(int, input().split()))

operator = list(map(int, input().split())) # 1 0 1 0
order = [0]*N
maximum = int(-sys.maxsize)
minimum = int(sys.maxsize)

def calculate():
    result = arr[0]
    for i in range(0, N-1):
        if(order[i]==0):
            result = result+arr[i+1]
        elif(order[i]==1):
            result = result-arr[i+1]
        elif(order[i]==2):
            result = result*arr[i+1]
        elif(order[i]==3):
            result = int(result/arr[i+1])
    return result
def solve(num):
    global maximum, minimum
    if(num==N-1):
        value = calculate()
        maximum = max(maximum, value)
        minimum = min(minimum, value)
    else:
        for i in range(4):
            if(operator[i]>=1):
                operator[i]-=1
                order[num]=i
                solve(num+1)
                operator[i]+=1
                order[num]=0
solve(0)
print(maximum)
print(minimum)