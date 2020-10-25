"""
Keregessunk be pozitiv egesz szamokat addig, amig 0-t nem kapunk.
Ezutan irjuk ki, hogy melyik szam hanyszor szerepelt, egeszen a legnagyobb kapott szamig.

Pleda bemenet:
--------------------------------------------
1
1
2
1
5
0
--------------------------------------------


Pelda kimenet:
--------------------------------------------
1: 3
2: 1
3: 0
4: 0
5: 1
--------------------------------------------

Feltetelezhetjuk, hogy legalabb egy nem 0 szamot fogunk kapni.

"""
szam=1
list=[]

while szam != 0:
  szam=int(input())
  list.append(szam)

max = 0
idx=0

while idx < len(list):
  if list[idx] > max:
    max = list[idx]
  idx+=1

for i in range(1,max+1):
  print(str(i)+": "+str(list.count(i)))