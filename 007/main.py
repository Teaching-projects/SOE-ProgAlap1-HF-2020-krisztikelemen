egyenleg=0
index=0
list=[]

osszeg=int(input())
list.append(osszeg)
egyenleg = egyenleg + osszeg
if egyenleg > 0:
  egyenleg = int(egyenleg + egyenleg/20)
if egyenleg < 0:
  egyenleg = int(egyenleg + egyenleg/10)
index += 1

while index != 12:
  osszeg=int(input())
  list.append(osszeg)
  egyenleg = egyenleg - 2000 + osszeg
  if egyenleg > 0:
    egyenleg = int(egyenleg + egyenleg/20)
  if egyenleg < 0:
    egyenleg = int(egyenleg + egyenleg/10)
  index += 1
print(egyenleg)

sum=sum(list)
print(sum)
