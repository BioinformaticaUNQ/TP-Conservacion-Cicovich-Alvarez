import os
import platform
import pathlib
from Bio.Align.Applications import ClustalwCommandline
from Bio import SeqIO
from .utils import getRepositoryFilePath
from .blast import getClustalInput, getClustalInputPath

#def getClustalOutputPath(inFile):
#    fileName = os.path.basename(inFile)
#    return getRepositoryFilePath(fileName.replace("clustalIn", "clustalOut"))
def getClustalOutputPath(pId, E_VALUE_ESPERADO):
    return getRepositoryFilePath(pId + '_clustalOut[' + str(E_VALUE_ESPERADO) + '].aln')

#def align(inFile):
def align(pId, E_VALUE_ESPERADO):
    isWindows = platform.system().lower() == 'windows'
    if (isWindows):
        clustalw_cmd = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
        assert os.path.isfile(clustalw_cmd), "Clustal W executable missing"
    else:
        clustalw_cmd = 'clustalw'
    #outfile = getClustalOutputPath(inFile)
    getClustalInput(pId, E_VALUE_ESPERADO)
    inFile = getClustalInputPath(pId, E_VALUE_ESPERADO)
    outFile = getClustalOutputPath(pId, E_VALUE_ESPERADO)
    clustalw_cline = ClustalwCommandline(clustalw_cmd, infile=inFile, outfile=outFile) #, output='fasta')
    clustalw_cline()
    return pathlib.Path(outFile).read_text()

def getAlignment(pId, E_VALUE_ESPERADO):
    file = pathlib.Path(getClustalOutputPath(pId, E_VALUE_ESPERADO))
    if file.exists():
        return file.read_text()
    else:
        return align(pId, E_VALUE_ESPERADO)

def getAlignment_flat(pId, E_VALUE_ESPERADO):
    getAlignment(pId, E_VALUE_ESPERADO)
    fasta_file = getClustalOutputPath(pId, E_VALUE_ESPERADO)
    alignment = []
    for seq_record in SeqIO.parse(fasta_file, 'clustal'):  # (generator)
        alignment.append({ "id": seq_record.id, "sequence": str(seq_record.seq) })
    return alignment

if __name__ == '__main__':
    #print(getAlignment(r"C:/Users/esteban.cicovich/Desktop/UNQ/BioInf/Practica/TPFinal/TP-Final-Bioinformatica/repository/1LXA_clustalIn[1e-13].fasta"))
    print(getAlignment_flat('1LXA', 0.0000000000001))