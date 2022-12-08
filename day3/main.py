import string
tab = string.ascii_lowercase
joinedlist = string.ascii_lowercase + string.ascii_uppercase

sum = 0
with open("input.txt", "r") as f:  # mettre le nom correct
    for line in f:
        new_line = line.strip()

        # split in two part
        half = int(len(new_line)/2)
        part_1 = new_line[:half]
        part_2 = new_line[half:]

        # Get letter in common
        res = str(set(part_1).intersection(part_2)).replace(',', '').replace('{', '').replace('}', '').replace('\'', '')
        sum += joinedlist.index(res)+1


print(sum)




