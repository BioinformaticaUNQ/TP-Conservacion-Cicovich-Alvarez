from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import pdb
def getSecondaryStructure(pdbID):
    pdb.fetchInPDBFormat(pdbID)
    p = PDBParser()
    structure = p.get_structure(pdbID, "seq.pdb")
    model = structure[0]
    dssp = DSSP(model, "seq.pdb")
    seq = ""
    secStructure = ""
    for key in dssp.keys():
        seq = seq + dssp[key][1]
        secStructure = secStructure + dssp[key][2]
    print("Secuencia: ", seq + " de longitud " + str(len(seq)))
    print("Estructura secundaria: ", secStructure + " de longitud " + str(len(secStructure)))

getSecondaryStructure("1LXA")