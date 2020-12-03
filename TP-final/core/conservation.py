import math
def getName(line):
    return line[0:35]


def getSeq(line):
    return line[36:86]


def addToSeqs(line, seqs):
    if(len(getName(line).strip()) != 0):
        if (getName(line) in seqs):
            seqs[getName(line)] = seqs[getName(line)] + getSeq(line)
        else:
            seqs[getName(line)] = getSeq(line)

def getSeqs():
    filepath = 'aligned.fasta'
    seqs = {}
    fp = open(filepath)
    # Esto crea un map donde cada clave es el nombre y tiene como valor su secuencia ya alineada
    for i, line in enumerate(fp):
        if i > 3:
            addToSeqs(line, seqs)
    fp.close()
    return seqs

def calculateConservation(inlineAminoacids):
    #Calcula el nivel de conservacion es UNA COLUMNA de aminoacidos
    # El valor estará entre 0 y 1 -0 -> no conservado,1 -> 100% conservado-
    ## PREGUNTAR :  Que pasa si la poteina original ingresada por el usuario no tiene ese aminoacido pero todos los demas si, se considera conservado? o.O
    aminos = {}
    for amino in inlineAminoacids:
        if(not amino in aminos):
            aminos[amino] = 1
        else:
            aminos[amino] = aminos[amino] + 1
    if('-' in aminos):del aminos['-']
    maxValue = max(list(aminos.values()))
    return round(maxValue / len(inlineAminoacids)* 100,3)


def calculateConsevedZone(porcentage):
    seqs = getSeqs()
    matching = []
    original = seqs[list(seqs.keys())[0]]
    i = 0
    for a in original:
        inlineAminoacids= []
        for v in list(seqs.values()):
            if(len(v) > i):
                inlineAminoacids.append(v[i])
            else:
                # Agrega - para cuando los alineamientos son de distinto tamaño
                inlineAminoacids.append("-")
        i+=1
        matching.append((a, calculateConservation(inlineAminoacids)))
    return matching

def aminoOrMinus(pair, porcentage):
    if(pair[1]>=porcentage):
        return pair[0]
    else:
        return '-'

def filterByConservationPorcentage(porcentage, matching):
    # Se puede usar para obtener la secuencia solo con los aminoacidos que cumplen el porcentaje de conservacion
    return list(map(lambda pair: aminoOrMinus(pair, porcentage), matching))

cons = calculateConsevedZone(80)
print("Secuencia de pares (amino,porcentaje): \n")
print(str(cons) +  "\n")
print("Secuencia que cumple con el nivel de conservacion")
print(filterByConservationPorcentage(90,cons))
