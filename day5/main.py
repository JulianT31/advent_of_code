tab = [1 + 4 * i for i in range(0, 9)]

stock = [[], [], [], [], [], [], [], [], []]

current_line = 1

with open("input.txt", "r") as f:
    for line in f:
        # récupération des
        if current_line < 9:
            for index in range(len(tab)):
                i = tab[index]
                if line[i] != " ":
                    stock[index].append(line[i])

        if current_line == 10:
            for tab in stock:
                tab.reverse()
                # for i in range(len(tab)):
                #     if tab[i] == " ":
                #         del tab[i]
                #         i-=1

        # algo
        if current_line > 10:
            temp = [int(s) for s in line.split() if s.isdigit()]

            quantity = temp[0]
            fromm = temp[1]
            to = temp[2]

            # echange
            move_tab = stock[fromm - 1][:quantity]
            move_tab.reverse()
            stock[to - 1] += move_tab
            # remove
            stock[fromm - 1] = [stock[fromm - 1][i] for i in range(len(stock[fromm - 1])) if i > quantity]

        current_line += 1
        for i in range(len(stock)):
            print(i+1 , stock[i])

        print()

# for i in stock:
#     print(i)
