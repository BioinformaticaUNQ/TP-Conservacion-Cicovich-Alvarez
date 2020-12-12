from Bio import SeqIO
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import operator
import time
from tp_final.core import conservation, clustal, pdb


def fillWithGaps(seq, st):
    # Agrega los gaps que le faltan a las estructura para coincidir con la secuencia ya alineada
    res = ""
    structure = st
    for a in seq:
        if (a == '-'):
            res = res + '-'
        else:
            if (len(structure) > 0):
                res = res + structure[0]
                structure = structure[1:]
    return res


def getSecondaryStructure(pdbID):
    pdb.fetchInPDBFormat(pdbID)
    p = PDBParser()
    structure = p.get_structure(pdbID, pdb.getTemporaryPDBPath())
    model = structure[0]
    dssp = DSSP(model, pdb.getTemporaryPDBPath())
    seq = ""
    secStructure = ""
    for key in dssp.keys():
        seq = seq + dssp[key][1]
        secStructure = secStructure + dssp[key][2]
    # print("Secuencia: ", seq + " de longitud " + str(len(seq)))
    # print("Estructura secundaria: ", secStructure + " de longitud " + str(len(secStructure)))
    return secStructure


def calculateConservation(inlineStructures):
    # Devuelve un par (P,porcentaje) donde P es el aminoacido con mayor apariciones.
    # Calcula el nivel de conservacion es UNA COLUMNA de pliegues
    structures = {}
    for st in inlineStructures:
        if (not st in structures):
            structures[st] = 1
        else:
            structures[st] = structures[st] + 1
    maxx = ('-', 0)
    for key, value in structures.items():
        if value > maxx[1] and '-' != key:
            maxx = (key, value)
    return maxx[0], round(maxx[1] / len(inlineStructures) * 100, 3)


def calculateConservedZone(structures):
    res = []
    first = structures[0]
    i = 0
    for s in first:
        inline = [s]
        for st in structures[1:]:
            if (len(st) > i):
                inline.append(st[i])
        i += 1
        res.append(calculateConservation(inline))
    return res


def calculateSecondaryStructureConservation(pdbId, E_VALUE):
    structures = []
    for record in SeqIO.parse(clustal.getAlignmentFile(pdbId, E_VALUE), 'clustal'):
        gapped = fillWithGaps(record.seq, getSecondaryStructure(record.id[5:9]))
        structures.append(gapped)
        time.sleep(0.5)
    return calculateConservedZone(structures)


def filterByConservationPorcentage(porcentage, matching):
    # Se puede usar para obtener la secuencia solo con los pliegues que cumplen el porcentaje de conservacion
    ls = list(map(lambda pair: conservation.aminoOrMinus(pair, porcentage), matching))
    return conservation.foldr(operator.add, '', ls)


def calculateSecondaryStructureConservation_json(pdbId, E_VALUE, percentage):
    conservation = calculateSecondaryStructureConservation(pdbId, E_VALUE)
    consensusFiltered = filterByConservationPorcentage(percentage, conservation)
    return {"conservation": conservation, "filterPercentage": percentage, "consensusFiltered": consensusFiltered}


if __name__ == '__main__':
    print(filterByConservationPorcentage(80, calculateSecondaryStructureConservation('1LXA', 0.0000000000001)))
