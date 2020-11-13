"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""
def initialize_map (width, height):
    terkep = []
    sor = []
    for y in range (1, height+1):
        for x in range (1, width+1):
            if (x == 1 or x == width) or (y == 1 or y == height):
                sor.append("██")
            else: 
                sor.append("░░")
        terkep.append(sor)
        sor = []
    return terkep

def pretty_map_print(map, character):
    x = character["position"]["x"]
    y = character["position"]["y"]
    width = len(map[1])
    height = len(map)
    
    if (x <= width - 1 and x >= 0) and (y <= height - 1 and y >= 0): 
        map[y][x] = "🧙"

    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end='')
        print()

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
