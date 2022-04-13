#by Julian Hastler aka.SKIP 04/13/2022
import random

rlist = []
print("Namen mit Enter bestätigen,\n"
     "wenn Ende mit # und Enter beenden.")
while True:
    ruser = input('')
    if ruser == '#':
        break
    else:
        rlist.append(str(ruser))
a = (len(rlist))
print(a , str("Namen eingetragen."))
print(rlist)
rabfrage = random.choice(rlist)
print("User:" , (rabfrage) , "du bist.")

input("Enter drücken zum beenden")