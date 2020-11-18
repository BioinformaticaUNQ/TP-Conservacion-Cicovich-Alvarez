import math


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

print(createFasta("homo-sapiens", "1231233", "ASDGGPALFGDMGMKMVIMAMSKMMGIDJASMFKASMFKDAFMKDFMIADFaASDASDSADASDASDASDASDASDASDASDASDASDAS"))
print(len("ASDGGPALFGDMGMKMVIMAMSKMMGIDJASMFKASMFKDAFMKDFMIADFaASDASDSADASDASDASDASDASDASDA"))
