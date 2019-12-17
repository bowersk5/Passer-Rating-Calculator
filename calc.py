#passer rating calculator based on NFL rules

a1 = int(input("How many completions? "))
a2 = int(input("How many attempts? "))
b1 = int(input("How many yards? "))
c1 = int(input("How many touchdowns? "))
d1 = int(input("How many interceptions? "))

a = ((a1/a2)-.3)*5 #((completions/attempts)-.3)*5
b = ((b1/a2)-3)*.25 #((yards/attempts)-3)*.25
c = (c1/a2)*20 #(touchdowns/attempts)*20
d = 2.375-((d1/a2)*25) #2.375 - ((interceptions/attempts)*25)

rating = ((a+b+c+d)/6)*100
rating = round(rating, 1) #round to 1 decimal point

while True:
  if a1 > a2:
    print("That is not possible.") # cannot have more completions than attempts
    break
  elif rating > 158.3: # max rating is 158.3
    print("Passer rating is : 158.3")
    break

# for NFL calculations, calculations can not be above 2.375
  elif a > 2.375:
    a = 2.375
    break
  elif b > 2.375:
    b = 2.375
    break
  elif c > 2.375:
    c = 2.375
    break
  elif d > 2.375:
    d = 2.375
    break

#for NFL calculations, calculations cannot be below 0
  elif a <= 0:
    a = 0 
    break
  elif b <= 0:
    b = 0
    break
  elif c <= 0:
    c = 0
    break
  elif d <= 0:
    d = 0
    break

#print
  else:
    print("Passer rating is :", rating)
    exit()
