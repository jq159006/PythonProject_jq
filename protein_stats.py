import os

my_file = os.path.join('data', 'AlphaLasso_20261102_154409.tsv')

# Initialize variables and groups
total_plddt = 0
total_area = 0
total_length = 0
count = 0

groups = {}

# Open and read the TSV file
with open(my_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    # extract values
    for line in lines[1:]:
        parts = line.strip().split('\t')

        lasso_type = parts[0]
        plddt_chain = float(parts[5])
        loop_area = float(parts[7])
        loop_length = float(parts[8])

        # Identify the main lasso group
        lasso_group = 'L' + lasso_type[2]

        # Accumulate overall totals and count
        total_plddt = total_plddt + plddt_chain
        total_area = total_area + loop_area
        total_length = total_length + loop_length
        count = count + 1

        # Initialize a group when first encountered
        if lasso_group not in groups:
            groups[lasso_group] = {
                'count': 0,
                'total_plddt': 0,
                'total_area': 0,
                'total_length': 0
            }

        # Accumulate totals and count within each group
        groups[lasso_group]['count'] += 1
        groups[lasso_group]['total_plddt'] += plddt_chain
        groups[lasso_group]['total_area'] += loop_area
        groups[lasso_group]['total_length'] += loop_length

# Calculate and print overall averages
avg_plddt = total_plddt / count
avg_area = total_area / count
avg_length = total_length / count

print('Overall')
print('Number of records:', count)
print('Average pLDDT_chain:', avg_plddt)
print('Average Loop_area:', avg_area)
print('Average Loop_length:', avg_length)
print('---' * 60)

# Calculate and print averages for each group
for lasso_group in sorted(groups):
    group_count = groups[lasso_group]['count']

    group_avg_plddt = groups[lasso_group]['total_plddt'] / group_count
    group_avg_area = groups[lasso_group]['total_area'] / group_count
    group_avg_length = groups[lasso_group]['total_length'] / group_count

    print('Lasso group:', lasso_group)
    print('Number of records:', group_count)
    print('Average pLDDT_chain:', group_avg_plddt)
    print('Average Loop_area:', group_avg_area)
    print('Average Loop_length:', group_avg_length)
    print('---' * 60)

#write the results to a CSV file
output_file = os.path.join('data', 'lasso_proteins_stats.csv')

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('Lasso_group,Average_pLDDT_chain,Average_Loop_area,Average_Loop_length\n')
    f.write(f'Overall,{avg_plddt},{avg_area},{avg_length}\n')

    for lasso_group in sorted(groups):
        group_count = groups[lasso_group]['count']

        group_avg_plddt = groups[lasso_group]['total_plddt'] / group_count
        group_avg_area = groups[lasso_group]['total_area'] / group_count
        group_avg_length = groups[lasso_group]['total_length'] / group_count

        f.write(f'{lasso_group},{group_avg_plddt},{group_avg_area},{group_avg_length}\n')

print('Results saved to:', output_file)