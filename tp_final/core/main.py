from tp_final.core import blast, clustal, conservation, pdb

PDB_ID="1LXA"
E_VALUE_REQUERIDO= 0.0000000000001
CONSERVATION_PORCENTAGE=80
pdb.fetchFromPDB(PDB_ID)
# Busca el pdbID en PDB y deja el fasta en seq.fasta
print(blast.getClustalInput(PDB_ID, E_VALUE_REQUERIDO))
# Levanta el seq y hace busqueda de similitud secuencial. Deja en clustal.fasta las secuencias homologas.
clustal.getAlignment_flat(PDB_ID, E_VALUE_REQUERIDO)
print("Alineamiento por Clustalw exitoso")
conservation.calculateConservedZone(PDB_ID, E_VALUE_REQUERIDO, CONSERVATION_PORCENTAGE)