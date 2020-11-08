"""
Tovabbfejlesztjuk az elozo dolgot. 

Most megirunk egy "szepen kiirato" fuggvenyt, ami megkap egy map-et, es az alabbi formaban kiirja a kimenetre:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


ha ez volt a bemenet:

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

tehat pl egy initialize_map(10,6) altal adott terkepet ha kiiratunk, az igy nezzen ki:
██████████
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
██████████

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

def pretty_map_print(map):
    for i in range (len(map)):
        for x in range (len(map[i])):
            print(map[i][x], end = "")
        print()


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
pretty_map_print(initialize_map(width,height))
