import os
from Bio.Align.Applications import ClustalwCommandline


def align(windows):
    if (windows):
        clustalw_exe = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
        fasta_file = os.path.join(os.getcwd(), 'TP-Final', 'core', 'SecuenciasCytocromoC.fasta')
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_file, outfile='aligned.fasta')
        assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
    else:
        in_file = 'clustal.fasta'
        clustalw_cline = ClustalwCommandline('clustalw', infile=in_file, outfile='aligned.fasta')
        clustalw_cline()
