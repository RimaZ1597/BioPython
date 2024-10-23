from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"

data=Entrez.esearch(db="nucleotide",term="BRCA1",retmax=50,idtype="gi")

rec=Entrez.read(data)

print(rec)

print(rec["IdList"])
