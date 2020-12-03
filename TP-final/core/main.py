import pdb
import blast
import clustal
E_VALUE_REQUERIDO= 0.04
print(pdb.fetchFromPDB("1LXA"))
# Busca el pdbID en PDB y deja el fasta en seq.fasta
print(blast.search(E_VALUE_REQUERIDO))
# Levanta el seq y hace busqueda de similitud secuencial. Deja en clustal.fasta las secuencias homologas.
print(clustal)