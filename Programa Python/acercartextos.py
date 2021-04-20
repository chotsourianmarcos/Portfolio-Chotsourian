import random

filename = input("Escribe el nombre del archivo: ")
archivo = open(filename, 'r')
texto = archivo.read()
archivo.close()

textoseparado = texto.split('\n\n')

cantidad = len(textoseparado)

def separarpalabras(cantidad):
    while cantidad > 0:
        textoseparado[cantidad - 1] = textoseparado[cantidad - 1].split(' ')
        cantidad -= 1
separarpalabras(cantidad)


sumatoriadistancia = 0
def distancia(corpus):
    global sumatoriadistancia
    for x in corpus:
        for y in x:
            for z in corpus:
                if y in z:
                    trayecto = abs(corpus.index(x) - corpus.index(z)) 
                    sumatoriadistancia += trayecto
distancia(textoseparado)

conjunto = range(0, cantidad -1)
acercamientos = []

def acercamiento(corpus):
    varía1 = random.randint(0, cantidad - 1)
    varía2 = random.randint(0, cantidad - 1)
    global sumatoriadistancia
    global sumatoriadistanciabeta
    corpus[varía1], corpus[varía2] = corpus[varía2], corpus[varía1]
    def distanciaslocalesbeta(corpus):
        global sumatoriadistancia
        global sumatoriadistanciabeta
        sumatoriadistanciabeta = 0
        for x in corpus:
            for y in x:
                for z in corpus:
                    if y in z:
                        trayectobeta = abs(corpus.index(x) - corpus.index(z))
                        sumatoriadistanciabeta += trayectobeta
    distanciaslocalesbeta(corpus)
    if sumatoriadistanciabeta < sumatoriadistancia:
        sumatoriadistancia = sumatoriadistanciabeta
    else:
        corpus[varía2], corpus[varía1] = corpus[varía1], corpus[varía2]
    acercamientos.append(sumatoriadistancia)

def intento():
    veces = 25
    while veces > 0:
        acercamiento(textoseparado)
        veces -= 1
intento()
    
while acercamientos[len(acercamientos)-1] != acercamientos[len(acercamientos)-25]:
    intento()

for x in range(0, len(textoseparado)):
    textoseparado[x] = ' '.join(textoseparado[x])

txtfinal = '\n\n'.join(textoseparado)

f = open("resultado.txt", "w")
f.write(txtfinal)
f.close()