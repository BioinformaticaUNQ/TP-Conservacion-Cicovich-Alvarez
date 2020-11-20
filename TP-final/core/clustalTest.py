import os
from Bio.Align.Applications import ClustalwCommandline

clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
fasta_file = os.path.join(os.getcwd(), "TP-Final", "core", "SecuenciasCytocromoC.fasta")
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_file)
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
