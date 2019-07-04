import random

# Simple natural selection algorithm

bases = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') # Including the blank space
goal_organism = 'CONSEGUE MOISES'

# Generates first organism of our natural selection.
# 'Genome' is all random letters
def abiogenesis():
    return ''.join([random.choice(bases) for x in range(len(goal_organism))])

number_of_children = 100

def reproduce(parent_code, number_of_children):
    children = []
    for x in range(number_of_children):
        children.append(mutate(parent_code, mutation_rate))
    return children

mutation_rate = 0.05

def mutate(parent_code, mutation_rate):
    new_code = []    
    for charac in parent_code:
        if random.random() < mutation_rate:
            new_code.append(random.choice(bases))
        else:
            new_code.append(charac)
    return ''.join(new_code)

def natural_selection(organisms):
    fittest_organism = 0
    fittest_organism_code = ''
    for child in organisms:
        fittness = 0
        for x in range(len(child)):
            if child[x-1] == goal_organism[x-1]:
                fittness += 1
                if fittness >= fittest_organism:
                    fittest_organism = fittness
                    fittest_organism_code = child
    return fittest_organism_code

first_organism = abiogenesis()
surviving_organism = first_organism
generation = 1
organisms = [first_organism]

while surviving_organism != goal_organism:
    print('Generation: %s' % str(generation))
    surviving_organism = natural_selection(organisms)
    print('Fittest organisms genetic code: %s' % surviving_organism)
    organisms = reproduce(surviving_organism, number_of_children)
    generation += 1
    if generation > 1000: # Fix the loop bug that ocrr when the generations is more than 1000x
        break
