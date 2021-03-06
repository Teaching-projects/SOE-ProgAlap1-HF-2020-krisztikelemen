"""
Ebben a perogramban a celunk egy futasok adatait rogzito fajlok statisztikainak kiiratasa.

Az alap adatszerkezetunke gy ilyen dictionary:

{"position":(x,y), "timestamp":ts, "elavation:e}

ahol:
 - x es y meterben megadott koordinatak egy alap viszonyitasi ponthoz kepest
 - ts egy egesz timestamp, ami masodpercben mondja meg, mennyi ido telt el ejfel ota
 - e pedig egy folytonos, meterben mert ertek a tengerszint feletti magassagrol


egy gpx track nem mas, mint ilyen adatpontoknak egy listaja.

A feladatban tobb, esetenkent egymasra epulo fuggvenyt kell megirni, melyek errol a trackrol arulnak el informaciokat.

"""


def position_distance(p1,p2):
    import math
    a = (p1[0],p1[1])
    b = (p2[0],p2[1])
    distance = math.sqrt(((abs(a[0]-b[0]))**2) + ((abs(a[1]-b[1]))**2))
    return distance

def total_distance(gpx):
    totaldistance = 0
    for i in range(len(gpx)-1):
        distance = position_distance(gpx[i]["position"],gpx[i+1]["position"])
        totaldistance += distance
    return totaldistance

def total_time(gpx):
    totaltime = 0
    for i in range(len(gpx)-1):
        totaltime += gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
    return totaltime

def idle_time(gpx):
    idletime = 0
    for i in range(len(gpx)-1):
        if gpx[i+1]["position"] == gpx[i]["position"]:
            seconds = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
            idletime += seconds
    return idletime

def moving_time(gpx):
    movingtime = total_time(gpx) - idle_time(gpx)
    return movingtime

def pretty_time(seconds):
    prettytime = 0
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = ((seconds % 3600) % 60) % 60

    if h < 1:
        if m == 0:
            prettytime = "{:02d}:{:02d}".format(m, s)
        else:
            prettytime = "{}:{:02d}".format(m, s)
    else:
        prettytime = "{}:{:02d}:{:02d}".format(h, m, s)
    return prettytime

def total_ascent(gpx):
    totalascent = 0
    for i in range(len(gpx)-1):
        ascent = gpx[i+1]["elavation"] - gpx[i]["elavation"]
        if ascent > 0:
            totalascent += ascent
    return totalascent

def chop_after_distance(gpx, distance):
    total = total_distance(gpx)
    totaldistance = 0
    track = []

    if total < distance:
        return track
    else:
        for i in range(len(gpx)-1):
            dist = position_distance(gpx[i]["position"],gpx[i+1]["position"])
            totaldistance += dist
            track.append(gpx[i])
            if totaldistance >= distance:
                track.append(gpx[i+1])
                return track

def fastest_1k(gpx):
    min = total_time(chop_after_distance(gpx,1000))
    
    for i in range (len(gpx)):
        track2 = chop_after_distance(gpx[i:],1000)
        if total_time(track2) < min and total_time(track2) > 0:
            min = total_time(track2)

    for j in range (len(gpx)):
        track3 = chop_after_distance(gpx[j:],1000)
        if total_time(track3) == min:
            return track3

    

import pickle

infile=open(input(),"rb")
gpx=pickle.load(infile)
infile.close()

print("Run statistics:")
print(" - Total distance: {:.2f} km".format(total_distance(gpx)/1000))
print(" - Total time    : {}".format(pretty_time(total_time(gpx))))
print(" - Total time    : {}".format(pretty_time(moving_time(gpx))))
print(" - Total ascent  : {:.0f} m".format(total_ascent(gpx)))
print(" - Fastest 1k    : {}".format(pretty_time(total_time(fastest_1k(gpx)))))

