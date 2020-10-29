perc=[]
sms=[]
list=[]

for i in range(12):
  perc.append(int(input()))
  sms.append(int(input()))

havidij=int(input())
percdij=int(input())
smsdij=int(input())

for honap in range(12):
  szamla = (percdij*perc[honap]) + (smsdij*sms[honap])
  if szamla > havidij:
    list.append(szamla)
  else: 
    list.append(havidij)

print(list)
print(sum(list))