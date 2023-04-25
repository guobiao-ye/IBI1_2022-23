# The fuction:
def dna_sequence_classification(sequence):
    # Convert the input string to uppercase
    sequence = sequence.upper()

    # Find the index positions of the start and stop codons
    start_codon_site = sequence.index("ATG")
    stop_codon_site = sequence.index("TGA")

    # Calculate the distance between the start codon and the stop codon (Do not include the start and stop codon)
    distance = stop_codon_site - start_codon_site - 3
    # Calculate the percentage of coding sequence
    percentage = (distance) / len(sequence) * 100

    # Classify the sequence as protein-coding, non-coding, or unclear
    if percentage > 50:
        sequence_classification = "protein-coding"
    elif percentage < 10:
        sequence_classification = "non-coding"
    else:
        sequence_classification = "unclear"

    # Return the percentage of coding sequence and sequence classification as output.
    return distance, percentage, sequence_classification


# An example function call:
distance, percentage, classification = dna_sequence_classification("ATGgtcacactTGAgtcttgactaaac")
print(f"Distance between the start and stop codon: {distance}")
print(f"Percent coding sequence: {percentage:.2f}%")
print(f"Sequence classification: {classification}")