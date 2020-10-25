"""
Kerj be egesz szamokat addig, amig 0-t nem kapsz.
A vegen irj ki minden bekert szamot, de mindgyiket csak egyszer, es abban a sorrendben, ahogy az elso elofordulas tortent.

pl:

Bemenet:
1
2
3
4
3
2
4
7
5
6
7
0
Kimenet:
1
2
3
4
7
5
6
"""
szam=1
list=[]
egyediek=[]
index=0

while szam != 0:
  szam=int(input())
  list.append(szam)

while index < len(list):
  aktualis = list[index]
  index2 = 0
  bennevan = False
  while index2 < len(egyediek):
    if egyediek[index2] == aktualis:
      bennevan = True
    index2 += 1
  if not bennevan:
    egyediek.append(aktualis)
  index += 1

print(egyediek)