"""
Ez a program nem fog mast csinalni, mint inicializal nekunk egy "terkepet", ami nem lesz mas, mint egy listakbol allo lista. 

A kovetkezo terkep:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


peldaul igy lenne eltarolva egy listakbol allo listaban:

terkep = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","░"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

Tehat a terkep[0][0] a terkep bal felso sarkat tartalmazza, a terkep[0][1] a tole jobbra levo mezot, stb. A lista jobb felso sarka most a terkep[0][13], a jobb also pedig a terkep[8][13].

Ez egy "felulnezet" egy epuletre, ahol █ reprezentalj a falakat, es ░ a szabadon bejarhato teruletet.

Elso alkalommal most az a feladat, hogy irjatok egy olyan fuggvenyt, ami visszaad egy ilyen terkepet.
"""


def initialize_map (width, height):
    terkep = []
    sor = []
    for y in range (1, height+1):
        for x in range (1, width+1):
            if (x == 1 or x == width) or (y == 1 or y == height):
                sor.append("█")
            else: 
                sor.append("░")
        terkep.append(sor)
        sor = []
    return terkep


"""
peldaul az initialize_map(3,4) a kovetkezo listat adja vissza:
[["█","█","█"],["█","░","█"],["█","░","█"],["█","█","█"]]

Ami nem mas, mint:
[
    ["█","█","█"],
    ["█","░","█"],
    ["█","░","█"],
    ["█","█","█"]
]

Egy kicsit nagyobb pelda: initialize_map(10,6) eredmenye:
[
    ["█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","█","█","█","█","█","█","█","█","█"]
]
"""


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
print(initialize_map(width,height))
