from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"

data=Entrez.esearch(db="nucleotide",term="BRCA1",retmax=10,idtype="acc")

rec=Entrez.read(data)

print(rec)

print(rec["IdList"])


f=open("/home/rima/Desktop/biopython/ret.fasta","w")
data1=Entrez.efetch(db="nucleotide",id=",".join(rec["IdList"]),rettype="fasta",retmode="text")

print(data1.read(),file=f)
