#1759번 문제 (암호 만들기)
#백트래킹을 이용하였다

import sys

min_consonant = 2 #자음은 최소 2개
min_vowel = 1 #모음은 최소 1개

vowels = ['a','e','i','o','u']

def check(arr):
    consonant_cnt, vowel_cnt = 0, 0
    for i in arr:
        if i in vowels: vowel_cnt+=1
        else: consonant_cnt+=1
    return (consonant_cnt>1) and (vowel_cnt>0)

def back_tracking(arr):
    if (len(arr) == L):
        if check(arr):
            print("".join(arr))
        return
    for i in range(alphabet.index(arr[-1])+1,C):
        arr.append(alphabet[i])
        back_tracking(arr)
        arr.pop()

input = sys.stdin.readline
L, C = map(int, input().split()) #각각 암호의 길이와 주어지는 문자의 개수
alphabet = list(input().split()) #주어지는 문자들
alphabet.sort()

for i in range(C-L+1):
    arr=[alphabet[i]]
    back_tracking(arr)