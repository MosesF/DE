import numpy as np
import random
import datetime
import os
import func
import matplotlib.pyplot as plt

# Create folder to store outputs of graphs
folder = "trials/{}/".format(str(datetime.datetime.now()).replace(" ", "_").replace(":","-"))
os.makedirs(folder)

# Function to confirm that all points being generated and created are within bounds
def confirm_bounds(b, bounds):
    new_b = []
    for i in range(len(b)):
        if b[i] < bounds[i][0]:
            new_b.append(bounds[i][0])
        if b[i] > bounds[i][1]:
            new_b.append([i][1])
        if bounds[i][0] <= b[i] <= bounds[i][1]:
            new_b.append(b[i])
    return new_b

# The differential evolution function
def diffEvo(function, bounds, pop_size, f, cr, maxNFC):

    # Initialize the population and fill with values
    pop = []
    for i in range(0, pop_size):
        ind = []
        for j in range(len(bounds)):
            ind.append(random.uniform(bounds[j][0], bounds[j][1]))
        pop.append(ind)

    NFC = 0
    error = []
    count = 1
    # While there are still runs left to be done
    while(NFC < maxNFC):
        score = []  # Array to hold the score from the crossover/mutation
        for j in range(0, pop_size):
            testers = np.arange(0, pop_size)
            test = testers.tolist()
            test.remove(j)
            rndPoint = random.sample(test, 3)

            x1 = pop[rndPoint[0]]
            x2 = pop[rndPoint[1]]
            x3 = pop[rndPoint[2]]
            xT = pop[j]

            xS = [x2i - x3i for x2i, x3i in zip(x2, x3)]

            vD = [x1i + f * xSi for x1i, xSi in zip(x1, xS)]

            trial = []
            for k in range(len(xT)):
                crossover = random.random()
                if crossover <= cr:
                    trial.append(vD[k])
                else:
                    trial.append(xT[k])

            score_t = function(trial)
            score_tar = function(xT)
            NFC += 1

            if score_t < score_tar:
                pop[j] = trial
                score.append(score_t)

            else:
                score.append(score_tar)

        best = min(score)
        sol = pop[score.index(min(score))]

        error.append(best)

        print(count)
        print("{} Solution", sol)
        count += 1
    return best, error


pop_size = 100  # Variable to hold number of points
cr = 0.9  # Cross over rate
f = 0.8  # Mutation rate
n = 0
functions = [HCEFunc, BCFunc, DFunc, RoFunc, AFunc, GFunc, RaFunc, KFunc, WFunc]
dimensions = [2, 5, 10]
bound = []
for j in range(len(dimensions)):
    d = dimensions[j]

    # Create an array for the bounds of points (-10,10)
    maxNFC = 3000 * d
    rr = [[] for i in range(int(maxNFC/pop_size))]

    rng = 10
    for i in range(d):
        bound.append((-rng, rng))

    for n in range(len(functions)):
        title = "DE for %s D%d" % (functions[n].__name__, d)
        print(title)

        for k in range(51):
            r = diffEvo(functions[n], bound, pop_size, f, cr, maxNFC)[1]
            for i in range(len(r)):
                rr[i].append(r[i])
        avg_error = [np.average(t) for t in rr]


        xAxis = range(int(maxNFC / pop_size))
        plt.xlabel("Number of function calls")
        plt.ylabel("Average Fitness")
        plt.title(title)
        plt.plot(xAxis, avg_error, linestyle='-', label='average error')
        #plt.plot(xAxis, min_error, linestyle=':', label='min error')
        #plt.plot(xAxis, max_error, linestyle='-.', label='max error')
        legend = plt.legend(loc='upper right', shadow='False')
        plt.savefig("{}{}.png".format(folder, title))
        plt.clf()
