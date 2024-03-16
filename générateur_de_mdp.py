import random
import string

letters = string.ascii_letters
nbr_ttl = 0
pwd = ""

nbr_lettre = int(input("Combien veut tu de lettre dans ton mdp ? : "))

def res():
    resultat = ''.join(random.choices(letters))
    return(resultat)

while nbr_ttl != nbr_lettre:
    pwd = pwd + res()
    nbr_ttl += 1

print (pwd)