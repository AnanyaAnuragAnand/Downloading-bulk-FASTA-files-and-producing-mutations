seq = input("""enter nucleotide seq:""")
pos = int(input("enter position to be mutated:"))
res_old = input("looking for mutating which residue?:")
res_new = input("enter residue you want:")

new_pos = pos - 1
def replace_char_at_index(org_str, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str
new_seq = replace_char_at_index(seq, new_pos, res_new)
print(new_seq)

