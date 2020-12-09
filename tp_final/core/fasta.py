import requests
import pathlib
from .utils import getRepositoryFilePath

def getFastaPath(pId):
    return getRepositoryFilePath(pId + '.fasta')

def fetchFromRCSB(pId):
    url = 'https://www.rcsb.org/fasta/entry/' + pId
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 404:
        print("No existe secuencia con ese PDB id :(")
    else:
        open(getFastaPath(pId), 'wb').write(response.content)
    return response.content.decode("utf-8") 
    
def getFasta(pId):
    file = pathlib.Path(getFastaPath(pId))
    if file.exists():
        return file.read_text()
    else:
        return fetchFromRCSB(pId)

def getSequence(pId):
    return str(getFasta(pId)).split("\n")[1]

def createFasta(description, identifier, sequence):
    parsedSequence = ""
    counter = 1
    for char in sequence:
        if(counter % 80 == 0):
            parsedSequence = parsedSequence + char + "\n"
        else:
            parsedSequence = parsedSequence + char
        counter+=1
    return ">" + identifier + "|" + description + "\n" + parsedSequence

if __name__ == '__main__':
    #print(createFasta("homo-sapiens", "1231233", "ASDGGPALFGDMGMKMVIMAMSKMMGIDJASMFKASMFKDAFMKDFMIADFaASDASDSADASDASDASDASDASDASDASDASDASDAS"))
    #print(len("ASDGGPALFGDMGMKMVIMAMSKMMGIDJASMFKASMFKDAFMKDFMIADFaASDASDSADASDASDASDASDASDASDA"))
    print(getSequence('1LXA'))