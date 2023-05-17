# before doing this, Make sure you have installed pandas library by running the command "pip install pandas" on your terminal!!!!!!!!!!!!!
import pandas as pd

# Read BLOSUM62
blosum62 = pd.read_excel('C:/Users/yh/IBI1_2022-23/Practical11/BLOSUM.xlsx')




# Function to read sequence from a file
def read_fasta(file_path):
    content = open(file_path)
    for line in content:
        if line.startswith('>'):
            name = line.rstrip()
        else: 
            sequence = line.rstrip()
    return name, sequence





# Function to perform sequence alignment
def align_sequences(protein1, protein2):
    seq1 = protein1[1]
    seq1_name = protein1[0]
    seq2 = protein2[1]
    seq2_name = protein2[0]

    alignment_score = 0
    identical_count = 0
    alignment = ''
    for i in range(len(seq1)):
        # Get the column index of seq1[i]
        index = blosum62.columns.get_loc(seq1[i])

        # Get the row index of seq2[i]
        row = blosum62.iloc[:, 0].values.tolist().index(seq2[i])

        # Get the score
        score= blosum62.iloc[row, index]

        alignment_score += score
        if seq1[i] == seq2[i]:
            alignment += '|'
            identical_count += 1   
        else:
            alignment += ' '
    percentage_identity = (identical_count / len(seq1)) * 100


    # Output analysis
    tplt = '{0:^25}'
    print("Sequence 1:", tplt.format(seq1_name), seq1)
    print(' ' * 37, alignment)
    print("Sequence 2:", tplt.format(seq2_name), seq2)
    print("Alignment Score:", alignment_score)
    print("Percentage Identity:", percentage_identity, '%')


    # Return the results
    return alignment, alignment_score, percentage_identity




# Read sequence
human_sequence = read_fasta('C:/Users/yh/IBI1_2022-23/Practical11/ACE2_human.fa')
mouse_sequence = read_fasta('C:/Users/yh/IBI1_2022-23/Practical11/ACE2_mouse.fa')
cat_sequence = read_fasta('C:/Users/yh/IBI1_2022-23/Practical11/ACE2_cat.fa')




# Call the function to get analysis
align_sequences(human_sequence, mouse_sequence)
print('\n\n')
align_sequences(human_sequence, cat_sequence)
print('\n\n')
align_sequences(mouse_sequence, cat_sequence)
