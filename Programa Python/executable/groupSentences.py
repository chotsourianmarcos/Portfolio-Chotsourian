#This is my very first program.
#Input: .txt file containing sentences.
#Output: .txt file containing the same sentences reordered, putting them closer to each other if their words resemble.

#Este es mi primer programa.
#Input: archivo .txt conteniendo oraciones.
#Output: archivo .txt conteniendo las mismas oraciones reordenadas, poniendo más cerca a aquellas cuyas palabras se parecen.

#Date: 2019
#Author: Marcos Chotsourian

import random

language = 'e'
language = input("For English enter 'English'. Para Español ingrese 'Español':")

filename = 0
if"glish" in language:
    filename = input("Write the file's name, which must be in the executable's location: ")
else:
    filename = input("Escribe el nombre del archivo, que debe estar en la ubicación del ejecutable: ")


file = open(filename, 'r')
texto = file.read()
file.close()

splittedText = texto.split('\n\n')

splittedTextCount = len(splittedText)

def splitWords(splittedTextCount):
    while splittedTextCount > 0:
        splittedText[splittedTextCount - 1] = splittedText[splittedTextCount - 1].split(' ')
        splittedTextCount -= 1
splitWords(splittedTextCount)


sentencesDistancesSum = 0
def calculateTotalDistances(corpus):
    global sentencesDistancesSum
    for x in corpus:
        for y in x:
            for z in corpus:
                if y in z:
                    trayecto = abs(corpus.index(x) - corpus.index(z)) 
                    sentencesDistancesSum += trayecto
calculateTotalDistances(splittedText)

#countRange = range(0, splittedTextCount -1)
stepsCloser = []

def stepCloser(corpus):
    changes1 = random.randint(0, splittedTextCount - 1)
    changes2 = random.randint(0, splittedTextCount - 1)
    global sentencesDistancesSum
    global sentencesDistancesSum2
    corpus[changes1], corpus[changes2] = corpus[changes2], corpus[changes1]
    def distanciaslocalesbeta(corpus):
        global sentencesDistancesSum
        global sentencesDistancesSum2
        sentencesDistancesSum2 = 0
        for x in corpus:
            for y in x:
                for z in corpus:
                    if y in z:
                        distance2 = abs(corpus.index(x) - corpus.index(z))
                        sentencesDistancesSum2 += distance2
    distanciaslocalesbeta(corpus)
    if sentencesDistancesSum2 < sentencesDistancesSum:
        sentencesDistancesSum = sentencesDistancesSum2
    else:
        corpus[changes2], corpus[changes1] = corpus[changes1], corpus[changes2]
    stepsCloser.append(sentencesDistancesSum)

def tryStepCloser():
    times = 25
    while times > 0:
        stepCloser(splittedText)
        times -= 1
tryStepCloser()
    
while stepsCloser[len(stepsCloser)-1] != stepsCloser[len(stepsCloser)-25]:
    tryStepCloser()

for x in range(0, len(splittedText)):
    splittedText[x] = ' '.join(splittedText[x])

finalTxt = '\n\n'.join(splittedText)

f = open("result.txt", "w")
f.write(finalTxt)
f.close()

if"glish" in language:
    print("Your file is ready.")
else:
    print("Su archivo está listo.")

exit = print()