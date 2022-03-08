from Bio import Entrez
from Bio import SeqIO

Entrez.email="ananyaanurag12@gmail.com"

input_id = input("enter id for downloading fasta file:")

handle=Entrez.efetch(db="nucleotide",id=input_id,rettype="fasta")
record=SeqIO.read(handle,"fasta")
outputname=f"C:/Users/anany/Desktop/{input_id}.fasta"
SeqIO.write(record, outputname, "fasta")
