
class Homology():
    idProt = ''
    sequence = ''
    
    def __init__(self, idProt="", sequence=""):
	    self.idProt = idProt
	    self.sequence = sequence

    def __str__(self):
        return self.idProt