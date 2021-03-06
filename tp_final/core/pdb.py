import requests
import pathlib
from tp_final.core.utils import getRepositoryFilePath, getRepositoryPath

def getPDBPath(pId):
    return getRepositoryFilePath(pId + '.pdb')

def fetchFromPDB(pdbId):
    url = 'https://files.rcsb.org/download/' + pdbId + '.pdb'
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 404:
        print("No existe secuencia con ese PDB id :(")
    else:
        open(getPDBPath(pdbId), 'wb').write(response.content)
        print("Se fetcheado el archivo fasta correctamente :D")
    return response.content.decode("utf-8") 
    
def getPDB(pId):
    file = pathlib.Path(getPDBPath(pId))
    if file.exists():
        return file.read_text()
    else:
        return fetchFromPDB(pId)

def fetchInPDBFormat(pdbId):
    url = 'https://files.rcsb.org/download/{}.pdb'.format(pdbId)
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 404:
        print("No existe secuencia con ese PDB id :(")
    else:
        open(getTemporaryPDBPath(), 'wb').write(response.content)
        print("Se fetcheado el archivo pdb correctamente :D")

def getTemporaryPDBPath():
    return getRepositoryFilePath('tmp.pdb')

if __name__ == '__main__':
    print(getPDB('1LXA'))