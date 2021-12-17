import string
from random import shuffle
import math

def caesar_flux(cuvant, cheie):
    pozitii_clar = []
    cod = ''

    for el in cuvant:
        pozitii_clar += [string.ascii_lowercase.index(el)]

    for i in range(len(pozitii_clar)):

        pozitii_clar[i] = (pozitii_clar[i] + cheie) % 26
    for el in pozitii_clar:
        cod += chr(el + 97)

    return cod

def caesar_blocuri(clar, chei, lungime_blocuri):
    blocuri = [clar[i:i+lungime_blocuri] for i in range(0, len(clar), lungime_blocuri)]
    cod = ''
    for i in range(len(blocuri)):
        cod += caesar_flux(blocuri[i], chei[i])
    return cod

if __name__ == '__main__':
    clar = input('Cuvantul de criptat: ')
    intrebari = ["Culoarea preferată: ", "Orașul nașterii: ", "Numele mamei: ", "Numele tatălui: ", "Mâncarea preferată: "]
    b = int(input('Lungimea blocurilor: '))
    raspunsuri = []

    for i in range(math.ceil(len(clar)/b)):
        shuffle(intrebari)
        raspunsuri += input(intrebari[i])
    
    chei = [string.ascii_lowercase.index(el[-1]) for el in raspunsuri]
    print(caesar_blocuri(clar, chei, b))