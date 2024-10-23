from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"

data=Entrez.efetch(db="nucleotide",id="2051982253,2052048926",rettype="fasta")

print(data.read())
