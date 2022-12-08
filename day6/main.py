nb_caract = 4  # part_1 => 4 & part_2 => 14

with open("input.txt", "r") as f:
    for line in f:
        for i in range(len(line) - nb_caract):
            # delete duplicate caract
            ens = set(line[i:i + nb_caract])
            # found a marker
            if len(ens) == nb_caract:
                break

# print solution
print(i + nb_caract)
