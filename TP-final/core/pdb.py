import requests


def fetchFromPDB(pdbId):
    url = 'https://www.rcsb.org/fasta/entry/' + pdbId
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 404:
        print("No existe secuencia con ese PDB id :(")
    else:
        open('seq.fasta', 'wb').write(response.content)
        print("Se fetcheado el archivo fasta correctamente :D")
