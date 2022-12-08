# index table of get value from stack
tab = [1 + 4 * i for i in range(0, 9)]

stock = [[], [], [], [], [], [], [], [], []]
current_line = 1

with open("input.txt", "r") as f:
    for line in f:
        # get init setup of stock
        if current_line < 9:
            for index in range(len(tab)):
                i = tab[index]
                if line[i] != " ":
                    stock[index].append(line[i])

        if current_line == 10:
            for tab in stock:
                tab.reverse()

        # algo
        if current_line > 10:
            # get instruction
            temp = [int(s) for s in line.split() if s.isdigit()]
            quantity = temp[0]
            fromm = temp[1]
            to = temp[2]

            # execute instruction
            move_tab = stock[fromm - 1][-quantity:]
            # move_tab.reverse() # remove for part 2
            stock[to - 1] += move_tab
            # remove
            stock[fromm - 1] = stock[fromm - 1][:-quantity]

        current_line += 1

# print the solution
for i in range(len(stock)):
    print(i + 1, stock[i])
