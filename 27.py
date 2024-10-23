from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"

data=Entrez.esearch(db="nucleotide",term="insulin",retmax="4",idtype="acc")

rec=Entrez.read(data)

print(rec)

print(rec["IdList"])

f=open("/home/rima/Desktop/biopython/result1.fasta","w")

data1=Entrez.efetch(db="nucleotide",id=",".join(rec["IdList"]),rettype="fasta")

print(data1.read(),file=f)
