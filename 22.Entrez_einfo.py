from Bio import Entrez

Entrez.email="zinjuwadiarima@gmail.com"   #it always tells to ncbi who we are

info=Entrez.einfo(db="nucleotide",term="insulin")   #einfo gives the info about databases in xml format

#data=info.read()

#print(data)

data=Entrez.read(info)  #this will convert the methods from xml to python object

print(data)

