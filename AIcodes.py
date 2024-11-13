# AI code 1
def iss(node,color,graph,colors):
    return all(colors[neighbor]!=color for neighbor in graph[node])
def sutil(graph,colors,m,node):
    if node == len(graph): return True
    for color in range(1,m+1):
        if iss(node,color,graph,colors):
            colors[node] = color
            if sutil(graph,colors,m,node+1): return True
            colors[node] = 0
    return False
def solve(graph,m):
    colors = [0]*len(graph)
    if not sutil(graph,colors,m,0):
        print("Solution does not exist")
        return
    for idx,color in enumerate(colors):
        print(f"Region {chr(65+idx)}: Color {color}")

n = int(input("Enter number of regions: "))
graph = [list(map(int, input(f"Connections for region {i} (end with -1): ").split()[:-1])) for i in range(n)]
m = int(input("Enter number of colors: "))
solve(graph,m)

# #Solution
# ❯ /bin/python /home/ar/Coding/py/AI1.py
# Enter number of regions: 4
# Connections for region 0 (end with -1): 1 2 -1
# Connections for region 1 (end with -1): 0 2 3 -1
# Connections for region 2 (end with -1): 0 1 3 -1
# Connections for region 3 (end with -1): 1 2 -1
# Enter number of colors: 3

# AI code 2

from constraint import Problem

def is_safe(f, g, w, c):
    return not (g == w and f != g) and not (g == c and f != g)

def farmer_wolf_goat_cabbage_puzzle():
    p = Problem()
    for var in ["farmer", "wolf", "goat", "cabbage"]:
        p.addVariable(var, [0, 1])
    p.addConstraint(is_safe, ["farmer", "wolf", "goat", "cabbage"])
    solutions = p.getSolutions()
    if solutions:
        for s in solutions:
            print(f"Farmer: {'Right' if s['farmer'] else 'Left'}, "
                  f"Wolf: {'Right' if s['wolf'] else 'Left'}, "
                  f"Goat: {'Right' if s['goat'] else 'Left'}, "
                  f"Cabbage: {'Right' if s['cabbage'] else 'Left'}")
    else:
        print("No solution exists")

farmer_wolf_goat_cabbage_puzzle()


# AI code 3

import random
def isv(b,r,c,num):
    return( num not in b[r]  and num not in [b[x][c]for x in range(9)] and num not in [b[i][j]for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)])
def s(b):
    for r in range(9):
        for c in range(9):
            if b[r][c] == 0:
                for num in random.sample(range(1,10),9):
                    if isv(b,r,c,num):
                        b[r][c]=num
                        if s(b): return True
                        b[r][c]=0
                return False
    return True
def gen(rc):
    b=[[0]*9 for _ in range(9)]
    s(b)
    for _ in range(rc):
        r,c=random.randint(0,8),random.randint(0,8)
        if b[r][c]:
            backup = b[r][c]
            b[r][c]=0
            if not s([r[:]for r in b]):b[r][c]=backup
    return b
def pr(b):
    for r in b:
        print(" ".join(str(num)if num else "_" for num in r))
if __name__=="__main__":
    pr(gen(0))

# AI code 4

import networkx as nx

def main():
    G = nx.DiGraph()
    for _ in range(int(input("Enter the number of edges: "))):
        u, v, w = input("Enter edge (source destination weight): ").split()
        G.add_edge(u, v, weight=float(w))

    source = input("Enter source: ")
    destination = input("Enter destination: ")

    try:
        path = nx.dijkstra_path(G, source, destination)
        length = nx.dijkstra_path_length(G, source, destination)
        print(f"Shortest path: {' -> '.join(path)} with length {length}")
    except nx.NetworkXNoPath:
        print(f"No path found from {source} to {destination}.")

if __name__ == "__main__":
    main()


# AI code 5

def bt(prior,like,evi):
    return (like*prior)/evi
prior = float(input("Enter prior probability of disease: "))
like = float(input("Enter likelihood of positive test: "))
no_like = float(input("Enter likelihood of negative test: "))
prior_null = 1-prior
evi = like*prior+no_like*prior_null
posterior_disease=bt(prior,like,evi)
print(f"P(Disese|Test)={posterior_disease:.4f}") 

# AI code 6

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('Attendance','Success_Predict'),('Participation','Success_Predict')])
cpd_a = TabularCPD('Attendance',2,[[0.7],[0.3]])
cpd_p = TabularCPD('Participation',2,[[0.5],[0.5]])
cpd_s = TabularCPD('Success_Predict',2,[[0.9,0.7,0.5,0.1],[0.1,0.3,0.5,0.9]],['Attendance','Participation'],[2,2])

model.add_cpds(cpd_a,cpd_p,cpd_s)
model.check_model()
print(VariableElimination(model).query(variables=['Success_Predict'],evidence={'Attendance':1,'Participation':1}))
