num_of_DNA, len_of_DNA = map(int, input().split())

# 각 자리에 대해 어떤 글자가 몇 번 나왔는기를 기록하기 위한 배열
loc_nucleo_info = [ {"A": 0, "C": 0, "G": 0, "T": 0} for _ in range(len_of_DNA) ]


for _ in range(num_of_DNA):
  DNA = input()
  for i in range(len_of_DNA):
    loc_nucleo_info[i][DNA[i]] += 1

min_HD_DNA = []
HD = 0
for ch_with_cnt in loc_nucleo_info:
  ch_with_cnt_list = list(ch_with_cnt.items())
  ch_with_cnt_list.sort(key=lambda x: (-x[1], x[0]))
  min_HD_DNA.append(ch_with_cnt_list[0][0])
  HD += ch_with_cnt_list[1][1] + ch_with_cnt_list[2][1] + ch_with_cnt_list[3][1]

print("".join(min_HD_DNA))
print(HD)