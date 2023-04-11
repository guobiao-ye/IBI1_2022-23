# Define the DNA sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

# Define the start codon and stop codons
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

# Initialize counters for coding sequences
count = 0

# Loop through the DNA sequence to find start and stop codons
for i in range(len(seq)):
    # Search for start codon
    if seq[i:i+3] == start_codon:
        for stop_codon in stop_codons:
            # Check if stop codon is found downstream from start codon
            if stop_codon in seq[i+3:]:
                # Increment coding sequence count
                count += 1

print("The total number of possible coding sequences is ", count)