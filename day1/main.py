# removing the new line characters
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

tab = []
sum = 0
for l in lines:
    if len(l) == 0 :
        tab.append(sum)
        sum = 0
    else :
        sum += int(l)

print(max(tab))
tab = sorted(tab)[-3:]
print(tab)

sum = 0
for i in tab:
    sum += i

print(sum)