from tkinter import OUTSIDE
from ast import While
import random


def passwordGenerator(passlenght, passuppercase, passlowercase, passfigures, passspecialchar):
    #Caractères possibles
    arrayuppercase = ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q',
                      'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N']
    arraylowercase = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q',
                      's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n']
    arrayspecialchar = ['&', 'é', '~', '"', '#', '{', '(', '[', '-', '|', 'è',
                        '_', 'ç', '^', 'à', '@', ')', ']', '+', '=', '}', '°', '$', '£', 'ù', '%', ',', ';', ':', '!']
    nbproperty = 0
    if passuppercase == 'o' or passuppercase == 'oui':
        nbproperty += 1
    if passlowercase == 'o' or passlowercase == 'oui':
        nbproperty += 1
    if passfigures == 'o' or passfigures == 'oui':
        nbproperty += 1
    if passspecialchar == 'o' or passspecialchar == 'oui':
        nbproperty += 1

    if nbproperty == 0:
        passlowercase = 'o'

    #longueur par type de char
    propertyLenghtfl = passlenght / nbproperty
    propertyLenght = int(propertyLenghtfl)

    #tableau des char du password
    arraypassupper = []
    arraypasslower = []
    arraypassfigure = []
    arraypassspecialchar = []

    #défini le mot de passe
    for i in range(1, propertyLenght+1):
        if passuppercase == 'o' or passuppercase == 'oui':
            elementupper = random.randint(0, len(arrayuppercase)-1)
            arraypassupper.append(arrayuppercase[elementupper])
        if passlowercase == 'o' or passlowercase == 'oui':
            elementlower = random.randint(0, len(arraylowercase)-1)
            arraypasslower.append(arraylowercase[elementlower])
        if passspecialchar == 'o' or passspecialchar == 'oui':
            elementspecial = random.randint(0, len(arrayspecialchar)-1)
            arraypassspecialchar.append(arrayspecialchar[elementspecial])
        if passfigures == 'o' or passfigures == 'oui':
            elementfigure = random.randint(0, 10)
            arraypassfigure.append(str(elementfigure))

    #array group
    allelement = []
    for i in arraypassupper:
        allelement.append(i)
    for i in arraypasslower:
        allelement.append(i)
    for i in arraypassfigure:
        allelement.append(i)
    for i in arraypassspecialchar:
        allelement.append(i)

    # Si manque de caracteres du fait de la division
    if len(allelement) < passlenght: 
        manquant = passlenght - len(allelement)
        resteaadd = 1
        while resteaadd <= manquant:
            choicearray = random.randint(0, 4)
            if choicearray == 0 and passuppercase == 'o' or passuppercase == 'oui':  # uppercase
                elementupper = random.randint(0, len(arrayuppercase)-1)
                allelement.append(arrayuppercase[elementupper])
            elif choicearray == 2 and passspecialchar == 'o' or passspecialchar == 'oui':
                elementspecial = random.randint(0, len(arrayspecialchar)-1)
                allelement.append(arrayspecialchar[elementspecial])
            elif choicearray == 3 and passfigures == 'o' or passfigures == 'oui':
                elementspecial = random.randint(0, 10)
                allelement.append(str(elementfigure))
            else:
                elementlower = random.randint(0, len(arraylowercase)-1)
                allelement.append(arraylowercase[elementlower])
            resteaadd += 1

    #désordonne le mot de passe
    random.shuffle(allelement)

    #password array --> password str
    realpassword = None
    for i in allelement:
        if realpassword == None:
            realpassword = i
        else:
            realpassword = realpassword + i


    print('\n\n')
    print('Votre mot de passe :\n ')
    print(realpassword)
    print('\n\n')



print('********* PASSWORD GENERATOR *********')

print('\nChoix des caractéristiques du mot de passe :')

print('Option conseillé ? (o, n)')
passadvised = input()

if passadvised == 'o':
    passlenght = 12
    passuppercase = 'oui'
    passlowercase = 'oui'
    passfigures = 'oui'
    passspecialchar = 'oui'
else:
    print('Nombre de caractères :')
    passlenght = int(input())

    while True:
        print('lettre majuscule ? (o, n)')
        passuppercase = input()
        if passuppercase == 'o' or passuppercase == 'n':
            break
        else:
            print('error')

    while True:
        print('chiffre ? (o, n)')
        passfigures = input()
        if passfigures == 'o' or passfigures == 'n':
            break
        else:
            print('error')

    while True:
        print('caractères spéciaux ? (o, n)')
        passspecialchar = input()
        if passspecialchar == 'o' or passspecialchar == 'n':
            break
        else:
            print('error')
    passlowercase = 'oui'

print('Caractèristiques :')
print('Longueur :', passlenght)
print('Majuscule :', passuppercase)
print('Minuscule :', passlowercase)
print('Chiffres :', passfigures)
print('Caractères spéciaux :', passspecialchar)

passwordGenerator(passlenght, passuppercase, passlowercase,
                  passfigures, passspecialchar)
