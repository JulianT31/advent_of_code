sum = 0
with open("input.txt", "r") as f:
    for line in f:
        start_1, end_1, start_2, end_2 = line.replace(",", "-").split("-")

        if start_1 < start_2 and end_1 > end_2:
            sum += 1

        elif start_2 < start_1 and end_2 > end_1:
            sum += 1

print(sum)
