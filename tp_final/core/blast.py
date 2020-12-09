from Bio.Blast import NCBIWWW, NCBIXML
from .fasta import getFasta
from .utils import getRepositoryFilePath
import pathlib

def getBlastPath(pId):
    return getRepositoryFilePath(pId + '_blast.xml')

def getClustalInputPath(pId, E_VALUE_ESPERADO):
    return getRepositoryFilePath(pId + '_clustalIn[' + str(E_VALUE_ESPERADO) + '].fasta')
    
def fetchFromBlast(pId):
    fasta_string = getFasta(pId)
    print("Buscando en Blast sobre internet... *Se recomienda preparar el mate*")
    result_handle = NCBIWWW.qblast("blastp", "pdb", fasta_string)
    # result_handle = open("my_blast.xml")
    #blast_records = NCBIXML.read(result_handle)
    #clustalFile = open(getBlastPath(pId), 'w')
    #clustalFile.write(blast_records)

    with open(getBlastPath(pId), "w") as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()

    blast_records = NCBIXML.parse(open(getBlastPath(pId)))
    return blast_records#.content.decode("utf-8") 

def getBlast(pId):
    file = pathlib.Path(getBlastPath(pId))
    if file.exists():
        return NCBIXML.parse(open(getBlastPath(pId)))
    else:
        return fetchFromBlast(pId)

def generateClustalInput(pId, E_VALUE_ESPERADO):
    blast_records = getBlast(pId)
    clustalFilePath = getClustalInputPath(pId, E_VALUE_ESPERADO)
    clustalFile = open(clustalFilePath, 'w')
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                # Filtra las secuencias que no son tan similares como queremos
                if hsp.expect < E_VALUE_ESPERADO:
                    print("****Alignment****")
                    print("sequence:", alignment.title)
                    print("length:", alignment.length)
                    print("e value:", hsp.expect)
                    print(hsp.query)
                    print(hsp.match)
                    print(hsp.sbjct)
                    clustalFile.write('>|' + alignment.title + '\n')
                    clustalFile.write(hsp.sbjct + '\n')
    clustalFile.close()
    return pathlib.Path(clustalFilePath).read_text()


def getClustalInput(pId, E_VALUE_ESPERADO):
    file = pathlib.Path(getClustalInputPath(pId, E_VALUE_ESPERADO))
    if file.exists():
        return file.read_text()
    else:
        return generateClustalInput(pId, E_VALUE_ESPERADO)

#https://www.rcsb.org/fasta/entry/1LXA
#https://files.rcsb.org/download/1LXA.pdb

# Lo correcto seria pegarle a uniprot y despues fijarse cual existe en pdb
#Sino
# Pegarle a pdb
# https://ftp.ncbi.nlm.nih.gov/blast/db/pdbaa.tar.gz
# 10 a la -10 PARAMETRIZAR


if __name__ == '__main__':
    print(getClustalInput('1LXA', 0.0000000000001))