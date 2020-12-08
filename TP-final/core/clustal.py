import os
import platform
from Bio.Align.Applications import ClustalwCommandline


def align():
    isWindows = platform.system().lower() == 'windows'
    if (isWindows):
        clustalw_exe = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
        fasta_file = os.path.join(os.getcwd(), 'TP-Final', 'core', 'SecuenciasCytocromoC.fasta')
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_file, outfile='aligned.fasta')
        assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
    else:
        in_file = 'clustal.fasta'
        clustalw_cline = ClustalwCommandline('clustalw', infile=in_file, outfile='aligned.fasta')
        clustalw_cline()

if __name__ == '__main__':
    align()