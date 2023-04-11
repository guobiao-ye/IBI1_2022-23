# Ask user to input stop codon
stop_codon = input("Please enter one of the three stop codons (TAA, TAG, TGA): ")

# Check if the input stop codon is valid
if stop_codon not in ['TAA', 'TAG', 'TGA']:
    print("Invalid stop codon. Please enter either TAA, TAG, or TGA.")
else:
    # Create output filename based on stop codon
    output_file = f"{stop_codon}_stop_genes.fa"

    # Input file path and name
    input_file = r'C:\Users\yh\IBI1_2022-23\Practical9\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

    # Open input file for reading
    with open(input_file, 'r') as f_in:
        # Open output file for writing
        with open(output_file, 'w') as f_out:
            # Initialize variables to store gene name and sequence count
            gene_name = None
            sequence_count = 0
            # Loop through each line in the input file
            for line in f_in:
                # Check if the line starts with '>' indicating a new gene entry
                if line.startswith('>'):
                    # Check if there is a previous gene entry
                    if gene_name is not None and gene_name.endswith(stop_codon):
                        # Write the gene name and sequence count to the output file in FASTA format
                        f_out.write(f'>{gene_name} ({sequence_count})\n')
                    # Extract the gene name from the line and remove other information
                    gene_name = line[1:].strip().split(' ')[0]
                    # Reset the sequence count variable
                    sequence_count = 0
                else:
                    # Concatenate the line to the sequence
                    f_out.write(line.strip())
                    sequence_count += 1

            # Check if there is a last gene entry at the end of the file
            if gene_name is not None and gene_name.endswith(stop_codon):
                # Write the last gene name and sequence count to the output file in FASTA format
                f_out.write(f'>{gene_name} ({sequence_count})\n')

    print(f"Extraction of genes ending with stop codon '{stop_codon}' completed.")
    print(f"Results saved in '{output_file}'")