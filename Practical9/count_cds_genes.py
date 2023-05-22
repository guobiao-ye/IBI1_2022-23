# Ask the user to input the stop codon
stop_codon = input("Enter one of the three stop codons (TAA, TAG, TGA): ")

# Create the output file name
output_file = f"{stop_codon}_stop_genes.fa"

# Open the input file for reading
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file:
    # Open the output file for writing
    with open(output_file, "w") as output_file:
        # Read the input file line by line
        lines = input_file.readlines()
        
        # Initialize variables
        gene_name = ""
        coding_sequence_count = 0
        sequence = ""
        
        # Process each line in the input file
        for line in lines:
            line = line.strip()
            
            # Check if the line contains the gene information
            if line.startswith(">"):
                # Check if we have a previous gene sequence to write
                if gene_name != "":
                    # Write the gene sequence in FASTA format to the output file
                    output_file.write(f">{gene_name} ({coding_sequence_count} coding sequences)\n")
                    output_file.write(f"{sequence}\n")
                
                # Extract the gene name from the line
                gene_name = line[1:].split(" ")[0]
                
                # Reset the coding sequence count and sequence
                coding_sequence_count = 0
                sequence = ""
            
            # Check if the line contains the sequence
            else:
                # Append the sequence to the existing sequence
                sequence += line
            
                # Count the number of coding sequences
                coding_sequence_count += line.count(stop_codon)
        
        # Write the last gene sequence to the output file
        output_file.write(f">{gene_name} ({coding_sequence_count} coding sequences)\n")
        output_file.write(f"{sequence}\n")

print(f"Extraction of genes ending with stop codon '{stop_codon}' completed.")
print(f"Results saved in '{output_file.name}'")
