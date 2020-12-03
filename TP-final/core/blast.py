from Bio.Blast import NCBIWWW, NCBIXML
import time
def search(E_VALUE_ESPERADO):
    fasta_string = open("seq.fasta").read()
    print("Buscando en Blast sobre internet... *Se recomienda preparar el mate*")
    result_handle = NCBIWWW.qblast("blastp", "pdb", fasta_string)
    blast_records = NCBIXML.read(result_handle)
    for alignment in blast_records.alignments:
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
                # clustalFile = open('clustal.fasta', 'wb')
                # clustalFile.write(alignment.title)
                # clustalFile.write(" query =")
                # clustalFile.write(alignment.query)
                # clustalFile.close()
    return "Busqueda de similitud secuelcial exitosa"


#https://www.rcsb.org/fasta/entry/1LXA
#https://files.rcsb.org/download/1LXA.pdb

# Lo correcto seria pegarle a uniprot y despues fijarse cual existe en pdb
#Sino
# Pegarle a pdb
# https://ftp.ncbi.nlm.nih.gov/blast/db/pdbaa.tar.gz
# 10 a la -10 PARAMETRIZAR

