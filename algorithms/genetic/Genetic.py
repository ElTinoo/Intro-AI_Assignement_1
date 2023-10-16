import random
from math import sqrt
from algorithms.genetic.Chromosome import Chromosome
from algorithms.genetic.Tile import Tile


def nRow(table):
    return len(table[0])


def nColumn(table):
    return len(table)


def nCell(table):
    return nRow(table) * nColumn(table)


def best_Fitness(parents, population):
    return [population[parents[0]].fitness, population[parents[0]].genome]


def defaultMaze():
    return [  # 1-->wall, 0-->void, 2-->start, 3-->end
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
         0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
         1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0,
         1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0,
         0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1,
         1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
         1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
         1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1,
         1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3,
         0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1]
    ]


"""
def population_Generator(tilesMatrix, tilesList, population_length):  # Generate the first population
    population = []
    for i in range(population_length):
        population.append(Chromosome(i, genome_Generator(tilesMatrix, tilesList), tilesList))

    return population


def genome_Generator(tilesMatrix, tilesList):
    genome_length = random.randint(nRow(tilesMatrix), int(nRow(tilesMatrix) * sqrt(2)))
    genome = [random.randint(0, len(tilesList))]  # Choose a random tile id
    jaja = 0
    while len(genome) < genome_length:  # building a genome around the randomly selected gene
        print(f"{jaja} | {genome}")
        jaja += 1
        match random.randint(0, 1):
            case 0:  # add gene before the first gene of the genome
                genome = [findNextGene(tilesMatrix, tilesList, genome, genome[0])] + genome
            case 1:  # add gene after the last gene of the genome
                genome.append(findNextGene(tilesMatrix, tilesList, genome, genome[-1]))

    return genome


def findNextGene(tilesMatrix, tilesList, genome, gene):  # Search the next gene to add after or before another gene
    nextGeneFound = False
    nextGeneId = -1
    while not nextGeneFound:
        match random.randint(0, 3):  # Randomize the position of the next gene
            case 0:  # next gene = right tile
                try:
                    nextGeneId = tilesMatrix[tilesList[gene].cooY][tilesList[gene].cooX + 1]
                except IndexError:
                    pass
            case 1:  # next gene = left tile
                try:
                    nextGeneId = tilesMatrix[tilesList[gene].cooY][tilesList[gene].cooX - 1]
                except IndexError:
                    pass
            case 2:  # next gene = bottom tile
                try:
                    nextGeneId = tilesMatrix[tilesList[gene].cooY + 1][tilesList[gene].cooX]
                except IndexError:
                    pass
            case 3:  # next gene = top tile
                try:
                    nextGeneId = tilesMatrix[tilesList[gene].cooY - 1][tilesList[gene].cooX]
                except IndexError:
                    pass
        if nextGeneId != -1 and nextGeneId not in genome:  # Stop condition
            nextGeneFound = True

    return nextGeneId
"""


def tilesGenerator(maze):  # Create Tiles according to the maze & convert maze into array same shape with Tiles ID
    tilesList = []
    tilesMatrix = [[0 for _ in range(nRow(maze))] for _ in range(nColumn(maze))]
    start_end_ID = []
    idP = 0
    for y in range(nColumn(maze)):
        for x in range(nRow(maze)):
            if maze[y][x] == 1:  # If it's a wall set the score to 1000, end or start 0, else 1
                tilesList.append(Tile(idP, x, y, 1000, maze[y][x]))
                tilesMatrix[y][x] = idP
            elif maze[y][x] == 3 or maze[y][x] == 2:
                start_end_ID.append(idP)
                tilesList.append(Tile(idP, x, y, 1, maze[y][x]))
                tilesMatrix[y][x] = idP
            else:
                tilesList.append(Tile(idP, x, y, 1, maze[y][x]))
                tilesMatrix[y][x] = idP
            idP += 1
    return tilesList, tilesMatrix, start_end_ID


def population_Generator(tilesMatrix, tilesList, populationLength, start_end_id):  # Generation of a population
    population = []
    for chromosomeID in range(populationLength):
        genome = []
        for geneID in range(random.randint(int(len(tilesMatrix[0])), int(len(tilesMatrix[0]) * sqrt(2)))):
            randomGene = random.randint(0, (len(tilesMatrix) * len(tilesMatrix[0])) - 1)
            if randomGene in genome:
                geneID += -1
            else:
                genome.append(randomGene)
        population.append(Chromosome(chromosomeID, genome, tilesList, start_end_id))
    return population


def selection(population, numberParents):  # select the 'numberOfBest' greatest chromosomes of the entire population
    parents = []
    fitnessList = []
    for chromosomeId in range(len(population)):
        fitnessList.append([population[chromosomeId].fitness, chromosomeId])
    fitnessList = sorted(fitnessList, key=lambda x: x[0])
    for parentsId in fitnessList[:numberParents]:
        parents.append(parentsId[1])
    return parents


def crossover(parentA_genome, parentB_genome):
    crossoverPoint = int((len(parentA_genome) + len(parentB_genome)) / 4)

    child_genome = parentA_genome[0:crossoverPoint]
    child_genome += (parentB_genome[crossoverPoint:])

    return child_genome


def new_Population(parents, population, numberOfChild, mutation_rate, tilesList, start_end_id):
    new_population = []
    idP = 0
    for i in range(0, len(parents), 2):
        for j in range(numberOfChild):
            parentA_genome, parentB_genome = population[parents[i]].genome, population[parents[i + 1]].genome
            child_genome = mutation(crossover(parentA_genome, parentB_genome), len(tilesList), mutation_rate)
            new_population.append(Chromosome(idP, child_genome, tilesList, start_end_id))
            idP += 1

    return new_population


def mutation(genome, nbrTiles, mutation_rate):  #
    for i in range(int(len(genome) * mutation_rate)):
        match random.randint(0, 2):
            case 0:  # add gene
                genome.append(random.randint(0, nbrTiles - 1))  # Add a random gene
            case 1:  # Remove gene
                del genome[random.randint(0, len(genome) - 1)]  # Delete a random gene
            case 2:  # Modify gene
                genome[random.randint(0, len(genome) - 1)] = random.randint(0, nbrTiles - 1)

    return genome


def evaluateTrend():  # Evaluation if we can stop the generations
    result = True
    return result


class Genetic:
    def __init__(self, population_length, numberOfChild, nGeneration, mutation_rate):
        if population_length % 4 != 0:
            print(f"!!! ----------------- Give a population length multiple of {numberOfChild} ----------------- !!!")
            exit(0)
        self._populationLength = population_length
        self._numberOfChild = numberOfChild
        self._numberParents = int(self._populationLength / numberOfChild)
        self._nbrGenerations = nGeneration
        self._mutation_rate = mutation_rate
        self._fitness = []
        self.fitness_trend = []
        self._parents = []
        self._childGenome = []
        self._mutedChildGenome = []
        self._bestScore = []
        self._tilesList, self._tilesMatrix, self._start_end_ID = tilesGenerator(defaultMaze())
        self._population = population_Generator(self._tilesMatrix, self._tilesList,
                                                self._populationLength, self._start_end_ID)
        self.start()

    def start(self):
        generation = 0
        while generation < self._nbrGenerations:
            self._parents = selection(self._population, self._numberParents)
            self._bestScore.append(best_Fitness(self._parents, self._population))
            self._population = new_Population(self._parents, self._population, self._numberOfChild, self._mutation_rate,
                                              self._tilesList, self._start_end_ID)
            generation += 1
        path = sorted(self._bestScore)[0][1]
        print(sorted(self._bestScore)[0])
        result = []
        for idTiles in path:
            result.append([self._tilesList[idTiles].cooX, self._tilesList[idTiles].cooY])
        return result

    def maze(self):
        return defaultMaze()
