import os, string, sys

import copy
from collections import deque

# appends padding spaces if the number is smaller than the largest value
# e.g. if the largest val=1245, 1 will be represented as '1   '
def format_num(n, maxSpaces):
    strNum = str(n)
    return strNum + ' ' * (maxSpaces - len(strNum))

# Just a wrapper over python dict to preserve things
# like height, width; also a pretty printing function provided
class Grid:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.d = d
    
    # pretty print the grid using the number formatter
    def pretty_print_grid(self):
        nSpaces = len(str(max(self.d.values()))) + 1
        strDelim = '|' + ('-' + (nSpaces * ' ')) * self.width + '|'
        print strDelim
        for y in range(self.height):
            print '|' + ' '.join([format_num(self.d[(x, y)], nSpaces) for x in range(self.width)]) + '|'
        print strDelim

# The grid is basically a dictionary. We can treat this as a graph where each node has 4 neighbors.
# Each neighbor contributes an in-edge as well as an out-edge.
# You might want to use this to construct you solution
class Graph:
    def __init__(self, grid):
        self.grid = grid
    
    def vertices(self):
        return self.grid.d.keys()
    
    def adj(self, (x, y)):
        return [u for u in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if u in self.grid.d.keys()]
    
    # put the value val for vertex u
    def putVal(self, u, val):
        self.grid.d[u] = val
    
    def getVal(self, u):
        return self.grid.d[u]


# Takes the grid and the points as arguments and returns a list of paths
# The grid represents the entire chip
# Each path represents the wire used to connect components represented by points
# Each path connects a pair of points in the points array; avoiding obstacles and other paths
# while minimizing the total path length required to connect all points
# If the points cannot be connected the function returns None
def find_paths(grid, points):
    # ---- Student Code ----
    G = Graph(grid)
    S = shortPath(G, points)
    actuals = []
    leftover = points
    whole = []
    least = S[0]
    actuals.append(least)
    whole += least
    for a in S[1:]:
        if not set(a)&set(whole):
            actuals.append(a)
            whole += a

    for cor in whole:
        if G.getVal(cor) == 0:
            G.putVal(cor,-1)
    
    for act in actuals:
        if (act[-1],act[0]) in points:
            leftover.remove((act[-1],act[0]))

    S = shortPath(G, leftover)
    for k in S:
        if not set(k)&set(whole):
            actuals.append(k)
            whole += k

    return actuals


def shortPath(G, points):
    
    possibles = []

    for p in points:
        p1 = p[0]
        p2 = p[1]
        b = bfs(G, p1, p2)
        #N = b.values()
        
        Q2 = []
        path = []
        Q2.append(b[p2])

        while len(Q2)>0:
            cur = Q2[0]
            Q2 = Q2[1:]
            path.append(cur.pos)
            if cur.parent:
                Q2.append(cur.parent)
            else:
                possibles.append(path)
                break

    possibles.sort(key = len)
    
    return possibles

def bfs(graph, start, end):
    Nodes = {}
    Q = []
    for el in graph.grid.d:
        n = Node(el,graph.getVal(el))
        Nodes[el] = n

    root = Nodes[start]
    root.distance = 0
    Q.append(start)

    while len(Q)>0:
        current = Q[0]
        Q = Q[1:]
        for ne in graph.adj(current):
            if Nodes[ne].val == -1:
                Nodes[ne].distance = -1
            if Nodes[ne].distance == "INF":
                Nodes[ne].distance = Nodes[current].distance + 1
                Nodes[ne].parent  = Nodes[current]
                if ne == end:
                    #print "done"
                    return Nodes
                elif ne != end:
                    Q.append(ne)
                else:
                    break
    return Nodes

class Node:
    def __init__(self,pos,val,distance="INF",parent=None):
        self.pos = pos
        self.val = val
        self.distance = distance
        self.parent = parent

# check that the paths do not cross each other, or the obstacles; returns False if any path does so
def check_correctness(paths, obstacles):
    s = set()

    for path in paths:
        for (x, y) in path:
            if (x, y) in s: return False
            for o in obstacles:
                if (o[0] <= x <= o[2]) and (o[1] <= y <= o[3]):
                    return False
            s.add((x, y))
    return True

def main():
    # read all the chip related info from the input file
    with open(sys.argv[1]) as f:
        # first two lines are grid height and width 
        h = int(f.readline())
        w = int(f.readline())
        
        # third line is the number of obstacles; following numObst lines are the obstacle co-ordinates
        numObst = int(f.readline())
        obstacles = []
        for n in range(numObst):
            line = f.readline()
            obstacles.append([int(x) for x in line.split()])
        
        # read the number of points and their co-ordinates
        numPoints = int(f.readline())
        points = []
        for n in range(numPoints):
            line = f.readline()
            pts = [int(x) for x in line.split()]
            points.append(((pts[0], pts[1]), (pts[2], pts[3])))
        print points
    grid = dict(((x, y), 0) for x in range(w) for y in range(h))
    # lay out the obstacles
    for o in obstacles:
        for x in range(o[0], o[2] + 1):
            for y in range(o[1], o[3] + 1):
                grid[(x, y)] = -1
    
    cnt = 1 # route count
    for (s, d) in points:
        grid[s] = cnt
        grid[d] = cnt
        cnt += 1
    
    numPaths = cnt - 1
    g = Grid(w, h, grid)
        
    g.pretty_print_grid()

    paths = find_paths(g, points)
    #print paths
    if paths is None:
        print "Cannot connect all the points!"
    else:
        # check the correctness
        if not check_correctness(paths, obstacles):
            raise ("Incorrect solution, some path cross each other or the obstacles!")
        print "Paths:"
        totLength = 0
        for p in paths:
            print p
            totLength += len(p)
        print "Total Length: " + str(totLength)
    
if __name__ == "__main__":
    main()

    