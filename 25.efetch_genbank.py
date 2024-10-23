from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"
f=open("/home/rima/Desktop/biopython/demo.gb","w")
data=Entrez.efetch(db="nucleotide",id="2051982253,2052048926",rettype="gb",retmode="text")

print(data.read(),file=f)
