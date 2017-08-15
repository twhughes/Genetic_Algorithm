from numpy.random import randint, rand
import matplotlib.pyplot as plt

OBJECTIVE = 15
POPULATION_SIZE = 200
DNA_LENGTH = 10
KILL_RATE = 0.1
NUM_CROSSOVERS = 4
MUTATION_RATE = 0.2

class Organism:
    DNA = ''
    def __init__(self):
        for i in range(DNA_LENGTH):
            self.DNA += str(randint(2))
        self.fitness = self.J(self.DNA)

    def J(self, DNA):
        return (OBJECTIVE-int(DNA, 2))**2

class Population:

    def __init__(self):
        self.organisms = []
        for i in range(POPULATION_SIZE):
            self.organisms.append(Organism())
        self.compute_avg_fitness()

    def display(self):
        for i in range(POPULATION_SIZE):
            print('organism ID = ' + str(i+1) + ', fitness = ', str(self.organisms[i].fitness))

    def compute_avg_fitness(self):
        self.avg_fitness = 0
        for i in range(POPULATION_SIZE):
            self.avg_fitness += self.organisms[i].fitness
        self.avg_fitness = self.avg_fitness/POPULATION_SIZE

    def kill_and_replace(self):
        num_to_kill = int(KILL_RATE*POPULATION_SIZE)
        self.organisms.sort(key = lambda x: x.fitness,reverse=True)
        for i in range(num_to_kill):
            parent_1 = self.organisms[randint(num_to_kill-1,POPULATION_SIZE)]
            parent_2 = self.organisms[randint(num_to_kill-1,POPULATION_SIZE)]
            new_DNA = self.crossover(parent_1.DNA,parent_2.DNA)            
            self.organisms[i] = Organism()
            self.organisms[i].DNA = new_DNA

    def crossover(self, DNA1, DNA2):
        crossover_pts = []
        for i in range(NUM_CROSSOVERS-1):
            crossover_pts.append(randint(DNA_LENGTH))
        crossover_pts.sort()
        DNA_new = ''
        i_prev = 0
        for i in range(len(crossover_pts)):
            i_current = crossover_pts[i]
            if (i%2==0):
                DNA_new += DNA1[i_prev:i_current]
            else:
                DNA_new += DNA2[i_prev:i_current]
            i_prev = i_current
        if (NUM_CROSSOVERS%2==1):
            DNA_new += DNA1[i_current:]
        else:
            DNA_new += DNA2[i_current:]

        return DNA_new


    def mutate(self):
        for i in range(POPULATION_SIZE):
            for j in range(DNA_LENGTH):
                if (rand() < MUTATION_RATE):
                    current_bit = self.organisms[i].DNA[j]
                    if (current_bit == '0'):
                        self.organisms[i].DNA = self.organisms[i].DNA[:j] + '1' + self.organisms[i].DNA[j+1:]
                    else:
                        self.organisms[i].DNA = self.organisms[i].DNA[:j] + '0' + self.organisms[i].DNA[j+1:]

    def life_cycle(self):
        self.compute_avg_fitness()        
        self.kill_and_replace()
        self.mutate()


if __name__=="__main__":
    N_generations = 1000
    fitness = []
    P = Population()
    for iter in range(N_generations):
        fitness.append(P.avg_fitness)
        P.life_cycle()

    P.display()
    plt.plot(fitness)
    plt.show()

    # breed
    # mutate