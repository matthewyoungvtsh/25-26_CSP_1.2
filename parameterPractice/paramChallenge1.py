def tic(num1, num2):
    tic_total = num1 - num2
    return tic_total

def tac(exp):
    y = 5
    exp = exp - 1
    for x in range(exp):
        y = y*5
        tac_total = y
    return tac_total


def toe():
    print(tic(3, 5))
    print(tac(4))

toe()