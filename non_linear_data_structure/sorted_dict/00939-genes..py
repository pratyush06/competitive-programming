# Gene dictionary with frozenset keys
gene = {
    frozenset(['dominant', 'dominant']): 'dominant',
    frozenset(['dominant', 'recessive']): 'dominant',
    frozenset(['recessive', 'recessive']): 'recessive',
    frozenset(['non-existent', 'recessive']): 'non-existent',
    frozenset(['non-existent', 'non-existent']): 'non-existent',
    frozenset(['non-existent', 'dominant']): 'recessive'
}

# Valid gene categories
gene_category = {'dominant', 'recessive', 'non-existent'}

# Dictionaries to store mappings
people_mapping = {}  # Maps person to their gene or None if not yet determined
parents = {}         # Maps child to list of parents

# Read number of input lines
N = int(input())

# Process input
for _ in range(N):
    person1, person2 = input().split()
    if person1 not in people_mapping:
        people_mapping[person1] = None
    if person2 in gene_category:
        people_mapping[person1] = person2  # person1 has a gene
    else:
        # person2 is a parent, add to parents list
        if person2 not in people_mapping:
            people_mapping[person2] = None
        if person2 not in parents:
            parents[person2] = []
        parents[person2].append(person1)

def find_ancestors(child):
    # Base case: if child already has a gene, return it
    if people_mapping.get(child) in gene_category:
        return people_mapping[child]
    
    # Get parents of the child
    parent_list = parents.get(child)
    if not parent_list or len(parent_list) < 2:
        return None  # Not enough parents to determine gene

    parent1, parent2 = parent_list[0], parent_list[1]
    
    # Recursively find genes for parents
    gene1 = people_mapping.get(parent1)
    if gene1 is None:
        gene1 = find_ancestors(parent1)
        people_mapping[parent1] = gene1

    gene2 = people_mapping.get(parent2)
    if gene2 is None:
        gene2 = find_ancestors(parent2)
        people_mapping[parent2] = gene2

    # If either parent's gene is None, return None (cannot determine)
    if gene1 is None or gene2 is None:
        return None

    # Look up the resulting gene using frozenset
    return gene.get(frozenset([gene1, gene2]), None)

# Compute genes for all children in parents dictionary
for child in parents:
    if people_mapping[child] is None:
        people_mapping[child] = find_ancestors(child)

# Print results in sorted order
sorted_people_mapping = {k: v for k, v in sorted(people_mapping.items()) if v is not None}
for person, gene_result in sorted_people_mapping.items():
    print(f'{person} {gene_result}')