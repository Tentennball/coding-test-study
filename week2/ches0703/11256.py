T = int(input())

for _ in range(T):
  candy, num_of_box = map(int, input().split())
  boxes = []
  for _ in range(num_of_box):
    r, c = map(int, input().split())
    boxes.append(r*c)

  boxes.sort(reverse=True)

  min_box = 0
  while candy > 0:
    candy -= boxes.pop(0)
    min_box += 1

  print(min_box)
