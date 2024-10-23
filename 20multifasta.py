from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence (5).fasta"

data=SeqIO.parse(path,"fasta")

for r in data:
	print(r.id)
	#print(r.seq)
	print("Count A",r.seq.count("A"))
	print("Count T",r.seq.count("T"))
	print("Count G",r.seq.count("G"))
	print("Count C",r.seq.count("C"))

	print("1st Frame :",r.seq.translate())
	print("2nd Frame :",r.seq[1:].translate())
	print("1ST Frame :",r.seq[2:].translate())
	
	rev=r.seq.reverse_complement()
	
	print("4th Frame :",rev.translate())
	print("5th Frame :",rev[1:].translate())
	print("6th Frame :",rev[2:].translate())
	
