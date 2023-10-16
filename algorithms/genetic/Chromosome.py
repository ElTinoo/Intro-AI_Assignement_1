def genomeFitness(genome, tilesList, start_end_id):
    score = 0

    if start_end_id[0] not in genome or start_end_id[1] not in genome:
        return 100000000000

    for gene in genome:
        score += tilesList[gene].tileScore
    return score


class Chromosome:
    def __init__(self, idP, genome, tilesList, start_end_id):
        self._id = idP
        self._genome = genome
        self._fitness = genomeFitness(genome, tilesList, start_end_id)

    @property
    def id(self):
        return self._id

    @property
    def genome(self):
        return self._genome

    @property
    def fitness(self):
        return self._fitness
