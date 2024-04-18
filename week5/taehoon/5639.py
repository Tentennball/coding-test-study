values = []

def travel(l, r):
    if(l>r): return

while(True):
    si = input()
    if not si:
        break
    values.append(int(si))

travel(0, len(values-1))