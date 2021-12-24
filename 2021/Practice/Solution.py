import operator
import os

from tqdm import tqdm

PART_SIZE = 100


def solve2(teams, pizzas):
    if len(pizzas) < 1:
        return
    for team in tqdm(teams):
        if len(pizzas) < 1:
            break
        maxScore = 0
        maxScoreIdx = 0
        for i, pizza in enumerate(pizzas[0:PART_SIZE]):
            score = team.calcSc(pizza)
            if score > maxScore:
                maxScore = score
                maxScoreIdx = i
        team.add(pizzas[maxScoreIdx])
        pizzas.pop(maxScoreIdx)


def solve(teams, pizzas):
    if len(pizzas) < 1:
        return
    for team in tqdm(teams):
        if len(pizzas) < 1:
            break
        for i in range(team.cap):
            maxScore = 0
            maxScoreIdx = 0
            for i, pizza in enumerate(pizzas[0:PART_SIZE]):
                score = team.calcSc(pizza)
                if score > maxScore:
                    maxScore = score
                    maxScoreIdx = i
            team.add(pizzas[maxScoreIdx])
            pizzas.pop(maxScoreIdx)


class Team():
    def __init__(self, cap):
        self.cap = cap
        self.pizzas = []
        self.ings = set()

    # @staticmethod
    # def calcScore(pizzas):
    #     uniq = set.union( [p.ings for p in pizzas] )
    #     total = 0
    #     for p in pizzas:
    #         total += p.count
    #     return len(uniq) / total

    def calcSc(self, pizza):
        comm = self.ings.intersection(pizza.ings)
        uniq = self.ings.union(pizza.ings)
        total = pizza.count
        for p in self.pizzas:
            total += p.count
        sc = len(uniq) - len(comm)  # (len(uniq)**2)/ (total)
        return sc

    def add(self, pizza):
        assert 1 + len(self.pizzas) <= self.cap
        self.pizzas.append(pizza)
        assert pizza.selected == False
        pizza.selected = True
        self.ings = self.ings.union(pizza.ings)

    def __repr__(self):
        return '[{}-{}-{}]'.format(self.cap, [p.index for p in self.pizzas], self.ings)

    @property
    def is_full(self):
        return len(self.pizzas) == self.cap


class Pizza(object):
    def __init__(self, index, ings):
        self.index = index
        self.ings = set(ings)
        self.count = len(self.ings)
        self.selected = False
        self.score = {}

    def __repr__(self):
        return '[id:{}-len:{}-{}]'.format(self.index, self.count, self.ings)


def readF(filename):
    f = open(filename)

    nPizza, n2, n3, n4 = [int(x) for x in f.readline().split(' ')[0:4]]

    pizzaL = []
    teamL2, teamL3, teamL4 = [], [], []
    unqPizza = set()
    total = 0
    for i in range(nPizza):
        ings = f.readline().replace('\n', '').split(' ')[1:]
        pizzaL.append(
            Pizza(i, ings)
        )
        unqPizza = unqPizza.union(pizzaL[-1].ings)
        total += len(pizzaL[-1].ings)

    for i in range(n2):
        teamL2.append(Team(2))
    for i in range(n3):
        teamL3.append(Team(3))
    for i in range(n4):
        teamL4.append(Team(4))

    print('------', filename)
    print('Avg Ings:', total/len(pizzaL))
    print('Total Pizza:', nPizza)
    print('Nums:', n2, n3, n4)
    print('Unique ings:', len(unqPizza))
    print('Total Cap:', n2*2 + n3*3 + n4*4)

    return nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4


def outF(filename, teamL2, teamL3, teamL4):
    f = open(filename, 'w+')
    nLine = 0
    for team in teamL4+teamL3+teamL2:
        if team.is_full:
            nLine += 1
    f.write(str(nLine) + '\n')
    for team in teamL4+teamL3+teamL2:
        if team.is_full:
            s = ' '.join([str(p.index) for p in team.pizzas])
            f.write('{} {}\n'.format(team.cap, s))
    f.close()


def solveAll(filename):
    nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4 = readF(filename)
    pizzaLSorted = sorted(
        pizzaL, key=operator.attrgetter('count'), reverse=True)
    solve(teamL4, pizzaLSorted)
    solve(teamL3, pizzaLSorted)
    solve(teamL2, pizzaLSorted)
    outF(filename.replace('data/', '')+'.out', teamL2, teamL3, teamL4)


solveAll("./Input/b_little_bit_of_everything.in")
solveAll("./Input/c_many_ingredients.in")
solveAll("./Input/d_many_pizzas.in")
solveAll("./Input/e_many_teams.in")
