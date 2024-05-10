import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

# 폴더명이 중복되지 않으므로 dict에 모든 폴더에 대해 정보를 저장
folder_dict = {}

for _ in range(N+M):
  parent, name, type = input().split()

  # 부모 폴더 정보가 dict에 없는 경우 빈 데이터 생성
  if parent not in folder_dict:
    folder_dict[parent] = {}
    folder_dict[parent]["files"] = []
    folder_dict[parent]['folders'] = []

  if type == '0':
    folder_dict[parent]["files"].append(name)
  elif type == '1':
    folder_dict[parent]["folders"].append(name)
    # dict에 하위 폴더에 대한 정보가 없는 경우 빈 데이터 생성
    if name not in folder_dict:
      folder_dict[name] = {}
      folder_dict[name]["files"] = []
      folder_dict[name]['folders'] = []

# 특정 폴더 내에 존재하는 모든 파일 검색
def file_check(folder):
  file_list = folder_dict[folder]["files"].copy()
  if folder_dict[folder]["folders"]:
    for child_folder in folder_dict[folder]["folders"]:
      file_list.extend(file_check(child_folder))
  return file_list


for _ in range(int(input())):
  folder = input().rstrip().split("/")[-1]
  file_list = file_check(folder)
  print(len(set(file_list)),len(file_list))


