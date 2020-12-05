import pdb
import blast
import clustal
import conservation

PDB_ID="1LXA"
E_VALUE_REQUERIDO= 0.0000000000001
CONSERVATION_PORCENTAGE=80
print(pdb.fetchFromPDB(PDB_ID))
# Busca el pdbID en PDB y deja el fasta en seq.fasta
print(blast.search(E_VALUE_REQUERIDO))
# Levanta el seq y hace busqueda de similitud secuencial. Deja en clustal.fasta las secuencias homologas.
clustal.align(False) # Si estas en windows cambia a True
print("Alineamiento por Clustalw exitoso")
conservation.calculateConservedZone(CONSERVATION_PORCENTAGE)