# linked nodes based code for implementation of TREE basics
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
#        self.weights = []

    class PreIterator:
        def __init__(self, st, gr):
            self.stk = [st]
            self.grf = gr
            self.seen = [False]*len(gr.vertices)

        def __next__(self):
            if len(self.stk) > 0:
                cur = self.stk[-1]
                del self.stk[-1]
                self.seen[cur] = True
                for c in reversed(self.grf.edges[cur]):
                    if self.seen[c] == False:
                        self.stk.append(c)
                return self.grf.vertices[cur]
            else:
                raise StopIteration

    def __iter__(self):
        return self.PreIterator(0, self) # 0 is index of starting vertex

    def addvertex(self, n):
#        if self.verices.index(n) >= 0:
#            raise Exeption("Vertex already exists")
        self.vertices.append(n)
        self.edges.append([])
#        self.weights.append([])

    def addedge(self, fr, to, wgt=None):
        frinx = self.vertices.index(fr)
        toinx = self.vertices.index(to)
        self.edges[frinx].append(toinx)
#        self.weights[frinx].append(wgt)

    def Display(self):
        seen = [False] * len(self.vertices)
        self.DisplayAux(0, 0, seen)
        print()

    def DisplayAux(self, r, level, seen):
        if r != None and seen[r] == False:
            seen[r] = True
            print("    "*level, self.vertices[r], sep="")
            for c in self.edges[r]:
                self.DisplayAux(c, level+1, seen)

# def main():
#     # Create a new GraphButNotGood
#     tg = Graph()
#     # add vertices to the Graph
#     tg.addvertex(10)
#     tg.addvertex(30)
#     tg.addvertex(80)
#     tg.addvertex(60)
#     tg.addvertex(40)
#     tg.addvertex(20)
#     tg.addvertex(70)
#     tg.addvertex(50)
#     # add edges to the Graph
#     tg.addedge(30, 10)
#     tg.addedge(30, 80)
#     tg.addedge(40, 10)
#     tg.addedge(20, 30)
#     tg.addedge(50, 70)
#     tg.addedge(10, 20)
#     tg.addedge(60, 20)
#     tg.addedge(60, 30)
#     tg.addedge(70, 50)
#     tg.addedge(30, 60)

#     # Display Graph data
#     print("Display Graph data")
#     tg.Display()

#     print()

#     print("OUTPUT of 'for d in tg:'")
#     for d in tg:
#         print(d)
#     print()

# main()