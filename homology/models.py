from tp_final.core.fastaCreator import getFasta

class Homology():
    idProt = ''
    sequence = ''
    
    def __init__(self, idProt):
	    self.idProt = idProt
	    self.sequence = getFasta(idProt)

    def __str__(self):
        return self.idProt