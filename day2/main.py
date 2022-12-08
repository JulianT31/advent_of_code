score_me = 0
score_op = 0

tab = ["A", "B", "C"]
tab_2 = ["X", "Y", "Z"]

with open("input.txt", "r") as f:  # mettre le nom correct
    for line in f:
        scores = line.split()
        me = tab.index(scores[0])
        op = tab_2.index(scores[1])

        # Victory
        if me == len(tab) - 1 and op == 0:
            score_op += (op + 1) + 6
            score_me += (me + 1)

        elif op == len(tab) - 1 and me == 0:
            score_me += (me + 1) + 6
            score_op += (op + 1)

        # Op win
        elif me - op == 1:
            score_op += (op + 1) + 6
            score_me += (me + 1)

        # Me win
        elif op - me == 1:
            score_me += (me + 1) + 6
            score_op += (op + 1)

        # Draw
        elif op == me:
            score_me += (me + 1) + 3
            score_op += (op + 1) + 3

print("score_me ", score_me)
print("score_op ", score_op)
