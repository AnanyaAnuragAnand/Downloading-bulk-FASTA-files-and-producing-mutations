from Bio import Entrez
from Bio import SeqIO

Entrez.email="ananyaanurag12@gmail.com"

f = open(file="C:/Users/anany/Desktop/COMP.BIO._PYTHON_SCRIPTS/acc_names.txt")
name_list = f.readlines()
print(name_list)

for name in name_list:

    input_id = name.strip()
    handle = Entrez.efetch(db="nuccore",id=input_id,rettype="fasta")
    record = SeqIO.read(handle,"fasta")
    outputname=f"C:/Users/anany/Desktop/{input_id}.fasta"
    SeqIO.write(record, outputname, "fasta")

    print(outputname)

    seq_data = open(f"C:/Users/anany/Desktop/{input_id}.fasta","r")
    count = 0
    seq = ''
    for line in seq_data.read().split("\n"):
        if count:
            seq += line
            # print(line, "line", count)
        else:
            count += 1
    
    pos = int(input("enter position to be mutated:"))
    new_pos = pos - 1

    p = list(seq)[new_pos]

    print(f"current nucleotide at this position is {p}")

    res_old = input("looking for mutating which residue?:")
    res_new = input("enter residue you want:")
    def replace_char_at_index(org_str, index, replacement):
        ''' Replace character at index in string org_str with the
        given replacement character.'''
        new_str = org_str
        if index < len(org_str):
            new_str = org_str[0:index] + replacement + org_str[index + 1:]
        return new_str
    new_seq = replace_char_at_index(seq, new_pos, res_new)

    f = open(f"C:/Users/anany/Desktop/{input_id}_mut.fasta", "w")
    new_outputname = f"C:/Users/anany/Desktop/{input_id}_mut.fasta"
    print(new_outputname)
    f.write(new_seq)
    f.close()
    