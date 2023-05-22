# Input file path and name
input_file = r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
# Output file path and name
output_file = r'TGA_genes.fa'

# Open input file for reading
with open(input_file, 'r') as f_in:
    # Open output file for writing
    with open(output_file, 'w') as f_out:
        # Initialize variables to store gene name and sequence
        gene_name = None
        sequence = ''
        # Loop through each line in the input file
        for line in f_in:
            # Remove leading and trailing whitespaces
            line = line.strip()
            # Check if the line starts with '>' indicating a new gene entry
            if line.startswith('>'):
                # Check if there is a previous gene entry
                if gene_name is not None and sequence.endswith('TGA'):
                    # Extract only the gene name from the previous gene entry
                    gene_name = gene_name.split(' ')[0]
                    # Write the gene name and sequence to the output file in FASTA format
                    f_out.write(f'>{gene_name}\n{sequence}\n')
                # Extract the gene name from the line
                gene_name = line[1:]  # Remove the '>' symbol
                # Reset the sequence variable
                sequence = ''
            else:
                # Concatenate the line to the sequence
                sequence += line
        # Check if there is a last gene entry at the end of the file
        if gene_name is not None and sequence.endswith('TGA'):
            # Extract only the gene name from the last gene entry
            gene_name = gene_name.split(' ')[0]
            # Write the last gene name and sequence to the output file in FASTA format
            f_out.write(f'>{gene_name}\n{sequence}\n')

print("Extraction of TGA genes completed. Results saved in TGA_genes.fa")
