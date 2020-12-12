from tp_final.core.fasta import getSequence

class Homology():
    idProt = ''
    sequence = ''
    filterEValue = ''
    filterConservationPersentage1 = 0
    filterConservationPersentage2 = 0
    
    def __init__(self, pID, filterEValue = '1e-10', filterConservationPersentage1 = 50, filterConservationPersentage2 = 50):
        self.idProt = pID
        self.sequence = getSequence(pID)
        self.filterEValue = filterEValue
        self.filterConservationPersentage1 = filterConservationPersentage1
        self.filterConservationPersentage2 = filterConservationPersentage2

    def __str__(self):
        return self.idProt