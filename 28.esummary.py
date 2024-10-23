from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"

data1=Entrez.esearch(db="nucleotide",term="BRCA1",retmax=50,idtype="gi")

rec=Entrez.read(data1)

print(rec)

print(rec["IdList"])
data=Entrez.esummary(db="nucleotide",id=",".join(rec["IdList"]))

record=Entrez.read(data)

#print(record)

for i in record:
	print("----------------------------")
	for a,b in i.items():
		print(a,b)
