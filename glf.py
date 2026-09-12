
while(True):
  me = float(input("Mosás előtt [g]: "))
  mu = float(input("Mosás után [g]: "))

  eredmeny = (100 * (me - mu)) / me

  print(f"Erdmény: {eredmeny:.2f}%\n")

  #aaaa