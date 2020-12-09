from tp_final.core.fasta import getSequence

class Homology():
    idProt = ''
    sequence = ''
    
    def __init__(self, idProt):
	    self.idProt = idProt
	    self.sequence = getSequence(idProt)

    def __str__(self):
        return self.idProt