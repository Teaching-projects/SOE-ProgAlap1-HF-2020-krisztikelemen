x=0.0
y=0.0

irany = input()

while irany != "stop":
  if irany == "forward":
    y = y + float(input())
  if irany == "backward":
    y = y - float(input())
  if irany == "right":
    x = x + float(input())
  if irany == "left":
    x = x - float(input())
  irany = input()

if irany == "stop":
  print(round(x,2))
  print(round(y,2))
  origo = ((x**2)+(y**2))**(1/2)
  print(round(origo,2))