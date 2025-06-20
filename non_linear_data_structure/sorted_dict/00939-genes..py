import unittest
import io
import sys

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

def process_genetics(input_data):
    # Reset global dictionaries for testing
    people_mapping = {}  # Maps person to their gene or None if not yet determined
    parents = {}         # Maps child to list of parents

    # Simulate input
    lines = input_data.strip().split('\n')
    N = int(lines[0])
    inputs = [line.split() for line in lines[1:]]

    # Process input
    for person1, person2 in inputs:
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

        # If either parent's gene is None, return None
        if gene1 is None or gene2 is None:
            return None

        # Look up the resulting gene using frozenset
        return gene.get(frozenset([gene1, gene2]), None)

    # Compute genes for all children in parents dictionary
    for child in parents:
        if people_mapping[child] is None:
            people_mapping[child] = find_ancestors(child)

    # Prepare output
    sorted_people_mapping = {k: v for k, v in sorted(people_mapping.items()) if v is not None}
    output = []
    for person, gene_result in sorted_people_mapping.items():
        output.append(f'{person} {gene_result}')
    return '\n'.join(output)

class TestGenetics(unittest.TestCase):
    def test_sample_input(self):
        # Sample input
        sample_input = """7
John dominant
Mary recessive
John Susan
Mary Susan
Peter non-existent
Susan Marta
Peter Marta"""

        # Expected output
        expected_output = """John dominant
Marta recessive
Mary recessive
Peter non-existent
Susan dominant"""
        # Process the input
        result = process_genetics(sample_input)

        # Compare result with expected output
        self.assertEqual(result.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()