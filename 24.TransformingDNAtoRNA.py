# Chapter1: Obtaining the sequences
# Let's use our knowledge of splitting and updating strings to transform DNA sequences into RNA sequences
# DNA and RNA encode information about our genetic material
# We represent them as sequences of letters, where each letter stands for a nucleotide.

sequences = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = sequences.split("#")
print(dna_list)


# Chapter2: Replacing
# With the DNA sequences stored in a list, we'll use a for loop to go through the list and convert each sequence into RNA.

for dna in dna_list:
    rna = dna.replace("t", "u")
    print("DNA: " + dna + " -> " + "RNA: " + rna)
