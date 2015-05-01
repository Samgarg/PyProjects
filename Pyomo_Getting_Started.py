__author__ = 'Davidws'

from pyomo.environ import *
model = AbstractModel()

model.vertices = Set()
model.edges = Set(within=model.verices*model.vertices)
model.ncolors = Param(within=PositiveIntegers)
model.colors = RangeSet(1, model.ncolors)

model.x = Var(model.vertices, model.edges, within = Binary)
model.y = Var()

def node_coloring_rule(model,v):
    return sum(model.x[v, c] for c in model.colors) == 1
model.node_coloring = Constraint(model.vertices, rule=node_coloring_rule)

def edge_coloring_rule(model, v, w, c):
    return model.x[v,c] + model.x[w,c] <= 1
model.edge_coloring = Constraint(model.edges, model.colors, rule=edge_coloring_rule)

def min_coloring_rule(model,v,c):
    return model.y >= c * model.x[v.c]
model.min_coloring = Constraint(model.vertices, model.colors, rule=min_coloring_rule)

model.obj = Objective(expr=model.y)

