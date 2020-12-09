from tp_final.core.fasta import getSequence

class Homology():
    idProt = ''
    sequence = ''
    filterEValue = ''
    filterConservationPersentage = 0
    
    def __init__(self, pID, filterEValue = '1e-10', filterConservationPersentage = 50):
        self.idProt = pID
        self.sequence = getSequence(pID)
        self.filterEValue = filterEValue
        self.filterConservationPersentage = filterConservationPersentage

    def __str__(self):
        return self.idProt