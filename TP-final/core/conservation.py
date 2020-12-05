from Bio import SeqIO


def getName(line):
    endOfName = 35
    for i in range(1, len(line)):
        if line[i:i + 6] == "      ":
            endOfName == i
            break
    return line[0:endOfName]


def getSeq(line):
    endOfName = 35
    for i in range(1, len(line)):
        if line[i:i + 6] == "      ":
            endOfName == i
            break
    return line[i + 6:i + 56]


def addToSeqs(line, seqs):
    if (len(getName(line).strip()) != 0):
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
    # Devuelve un par (A,porcentaje) donde A es el aminoacido con mayor apariciones.
    # Calcula el nivel de conservacion es UNA COLUMNA de aminoacidos
    aminos = {}
    for amino in inlineAminoacids:
        if (not amino in aminos):
            aminos[amino] = 1
        else:
            aminos[amino] = aminos[amino] + 1
    maxx = ('-', 0)
    for key, value in aminos.items():
        if value > maxx[1] and '-' != key:
            maxx = (key, value)
    return maxx[0], round(maxx[1] / len(inlineAminoacids) * 100, 3)


def calculateConservedZone(porcentage):
    seqs = SeqIO.parse('aligned.fasta', 'clustal')
    original = next(seqs)
    matching = []
    i = 0
    for a in original:
        inlineAminoacids = [a]
        for record in SeqIO.parse('aligned.fasta', 'clustal'):
            inlineAminoacids.append(record.seq[i])
        i += 1
        matching.append(calculateConservation(inlineAminoacids))
    print('Secuencia de pares (amino,porcentaje): \n')
    print(str(matching) + "\n")
    print(len(matching)," resultados")
    print("Secuencia que cumple con el nivel de conservacion")
    print(filterByConservationPorcentage(porcentage, matching))
    return matching


def aminoOrMinus(pair, porcentage):
    if (pair[1] >= porcentage):
        return pair[0]
    else:
        return '-'


def filterByConservationPorcentage(porcentage, matching):
    # Se puede usar para obtener la secuencia solo con los aminoacidos que cumplen el porcentaje de conservacion
    return list(map(lambda pair: aminoOrMinus(pair, porcentage), matching))
