"""
Irj programot, mely beker egy egesz szamot: n. Feltetelezhetjuk, hogy ez pozitiv. 

Ezt kovetoen kerjen be egesz szamokat addig, amig n db nemnegativ szamot nem kapott. 
A program a futasa vegen irja ki egy listaban ezeket a szamokat.

Pelda bemenet:
3
1
2
3
Pelda kimenet:
[1, 2, 3]

Pelda bemenet:
3
-1
0
-44
35
-19
-35
1
Pelda kimenet:
[0, 35, 1]

"""

n=int(input())
index=0
list=[]

while index != n:
    szam=int(input())
    if szam >= 0:
        index+=1
        list.append(szam)

print(list)