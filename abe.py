import string
import random
import asyncio
from unicodedata import normalize
from pyp import main

def eleccionLetras(abe):
    
    letrasDelTurno = []
    num = []
    while len(num) != 9:
        n = random.randint(0, len(abe) - 1)
        if n not in num:
            num.append(n)
    
    for n in num:
        letrasDelTurno.append(abe[n])

    return letrasDelTurno

def chequeo(pa, lets):

    nuevaList = []
    for l in lets:
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        l = normalize('NFKC', normalize('NFKD', l).translate(trans_tab))
        nuevaList.append(l)


    palabra = list(pa)
    control = []

    if pa == "-":
        print("\nNo pudiste armar una palabra, perdes un turno\n")
        control.append ("ok")
        return True

    if palabra == [] or len(palabra) <= 2:
        control.append("notOk")

    

    for letra in palabra:
        if letra in nuevaList:
            control.append("ok")
            nuevaList.remove(letra)
        else:
            control.append("notOk")

    if "notOk" in control:
        if len(nuevaList) < 9:
            usa = set(palabra)
            for letra in usa:
                nuevaList.append(letra)
            return False
    print("Espere un momento")
    cheq = asyncio.get_event_loop().run_until_complete(main(pa))
    if cheq == False:
        print("\nEsta palabra no existe segun la RAE")
        return False
    else:
            return True



def juego():

    print("======================")
    print("Buenvenido al pensante")
    print("======================")

    print("\nReglas: \nHay 75 letras del abecedario (algunas repetidas),\nPor turno recibiras 9 letras para formas cualquier palabra de 3 o mas letras\nTu objetivo es hacer palabras largas para mas puntos\n")


    abecedario = list(string.ascii_uppercase + string.ascii_uppercase +"Ñ" +"A"+"A"+"A"+"A"+"A"+"A"+"A"+"A" +"E"+"E"+"E"+"E"+"E"+"E" +"O"+"O"+"O"+"O"+"O"+"O"+"O" +"S"+"S"+"S"+"S" +"U"+"U"+ "R"+"R"+"R"+"R" +"N"+"N")
    palabrasHechas = []
    # letrasUsadas = []
    letrasDelTurno = []
    rounds = 5


    while rounds != 0:
        
        letrasDelTurno = eleccionLetras(abecedario)               

        print(f"ABC: {len(abecedario)}")
        print(f"\nTurnos = {rounds}")
        print(f"Palabras hechas: {palabrasHechas}")
        print(f"Letras restantes = {len(abecedario)}")
        print(f"Tus letras: {letrasDelTurno}")

        palabra = input("Arma una palabra, de no poder, escribir un guion ('-'): ").upper()

        chequear = False
        chequear = chequeo(palabra, letrasDelTurno)
        while chequear != True:

            men = ""
            if len(letrasDelTurno) < 9:
                men = "\nPerdiste letras por hacer el piola"

            print(f"\nTu palabra '{palabra}' no cumple con los requisitos, escriba otra\nDebe tener mas de dos letras y contener solo letras otorgadas{men}\n")
            print(f"\nTurnos = {rounds}")
            print(f"Palabras hechas: {palabrasHechas}")
            print(f"Cantidad de letras restantes = {len(abecedario)}")
            print(f"Tus letras: {letrasDelTurno}")
            palabra = input("Arma una palabra, de no poder, escribir '-': ").upper()
            chequear = chequeo(palabra, letrasDelTurno)

        if chequear == True:
            for letra in letrasDelTurno:
                abecedario.remove(letra)
                
            palabrasHechas.append(palabra)
            rounds -= 1


    PuntPoPalabra = []
    puntTotal = 0
    mensaje = ""

    for palabra in palabrasHechas:
        valorPalabra = 0
        if palabra == "-":
            valorPalabra = 0
        if len(palabra) == 1 or 2:
            valorPalabra = 0 
        if len(palabra) > 2:
            valorPalabra = len(palabra)
        junto = palabra + " / " + str(valorPalabra)
        PuntPoPalabra.append(junto)
        puntTotal += valorPalabra

    if puntTotal <= 5:
        mensaje = "Ni probaste padre :/"
    if puntTotal <= 10 and puntTotal > 5:
        mensaje = "Fatal :("
    if puntTotal < 20 and puntTotal > 10:
        mensaje = "Menos de 20 es bastante poco :|"
    if puntTotal == 20:
        mensaje = "20 no esta tan mal :p"
    if puntTotal > 20 and puntTotal <28:
        mensaje = "Mas de 20 esta bastante bien :)"
    if puntTotal >= 28:
        mensaje = "MUY buen puntaje <3"

    print(f"\nTermino el juego!\nFormaste estas palabras y te dieron estos puntos: {PuntPoPalabra}\nPuntacion total: {puntTotal}\n{mensaje}")


juego()


