import matplotlib.pyplot as plt

""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""


def translate_from_dna_to_rna(dna: str) -> str:
    rna = dna.replace('T', 'U')
    return rna


def count_nucleotides(dna: str) -> dict:
    num_of_nucleotides = dict.fromkeys(['A', 'C', 'G', 'T'], 0)
    for c in 'ACGT':
        num_of_nucleotides[c] = dna.count(c)
    return num_of_nucleotides


def translate_rna_to_protein(rna: str, codon_dict: dict) -> str:
    codon = ''
    protein = ''
    for c in rna:
        if len(codon) < 3:
            codon += c
        else:
            protein += codon_dict[codon]
            codon = c
    return protein


def plot_hist(values: dict, title: str, x='', y=''):
    plt.figure(title)
    plt.title(title)
    plt.bar(list(values.keys()), values.values())
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()


# Read the file dna.fasta
dna_file = open('files/dna.fasta', 'r')

# Create rna.fasta file
rna_file = open('files/rna.fasta', 'w')

# Write rna to the rna.fasta file
for line in dna_file:
    if line[0] == '>':
        rna_file.write(line)
    else:
        rna_file.write(translate_from_dna_to_rna(line))

# Close rna.fasta file
rna_file.close()

# Count number of nucleotides for which gene
dna_file.seek(0)
dna_lines = ''
num_of_nucleotides_lst = []
description_lst = []
for line in dna_file:
    if line[0] == '>':
        if dna_lines:
            num_of_nucleotides_lst.append(count_nucleotides(dna_lines))
            dna_lines = ''
            description_lst.append(line.replace('>', ''))
        else:
            description_lst.append(line.replace('>', ''))
    else:
        dna_lines += line
else:
    num_of_nucleotides_lst.append(count_nucleotides(dna_lines))

# Close dna.fasta file
dna_file.close()

# Print number of nucleotides for which gene and plot histogram
xlabel = 'Nucleotides'
ylabel = 'Frequency'
for i, number_of_nucleotides in enumerate(num_of_nucleotides_lst):
    print(description_lst[i], number_of_nucleotides)
    plot_hist(number_of_nucleotides, description_lst[i], xlabel, ylabel)

# Open rna_codon_table.txt file
rna_codon_file = open('files/rna_codon_table.txt', 'r')

# Get codon table
codon_dict = {}
for line in rna_codon_file:
    codon_lst = line.split()
    codon_dict.update(dict(zip(codon_lst[::2], codon_lst[1::2])))

# Close rna_codon_file
rna_codon_file.close()

# Open rna.fasta file in read mode
rna_file = open('files/rna.fasta', 'r')

# Create protein.fasta file
protein_file = open('files/protein.fasta', 'w')

# Transform rna to protein and write result to protein.fasta file
for line in rna_file:
    if line[0] == '>':
        protein_file.write(line)
    else:
        prot_line = translate_rna_to_protein(line, codon_dict)
        prot_line = prot_line.replace('Stop', '')   # Remove Stop if necessary
        protein_file.write(prot_line+'\n')

# Close protein.fasta file
protein_file.close()

# Close rna.fasta file
rna_file.close()
