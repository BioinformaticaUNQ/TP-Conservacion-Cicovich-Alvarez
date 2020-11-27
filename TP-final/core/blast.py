from Bio.Blast import NCBIWWW, NCBIXML
import time

E_VALUE_THRESH = 0.04
fasta_string = open("seq.fasta").read()
result_handle = NCBIWWW.qblast("blastp", "pdb", fasta_string)
blast_records = NCBIXML.read(result_handle)
for alignment in blast_records.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            #print("sequence:", alignment.title)
            #print("length:", alignment.length)
            print("e value:", hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)

print(result_handle)

#https://www.rcsb.org/fasta/entry/1LXA
#https://files.rcsb.org/download/1LXA.pdb

# Lo correcto seria pegarle a uniprot y despues fijarse cual existe en pdb
#Sino
# Pegarle a pdb
# https://ftp.ncbi.nlm.nih.gov/blast/db/pdbaa.tar.gz
# 10 a la -10 PARAMETRIZAR

