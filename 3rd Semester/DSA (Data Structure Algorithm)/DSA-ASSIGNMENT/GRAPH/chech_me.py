
from my_graph import *


def main():
    # Create a new GraphButNotGood
    tg = Graph()
    # add vertices to the Graph
    tg.addvertex(10)
    tg.addvertex(30)
    tg.addvertex(80)
    tg.addvertex(60)
    tg.addvertex(40)
    tg.addvertex(20)
    tg.addvertex(70)
    tg.addvertex(50)
    # add edges to the Graph
    tg.addedge(30, 10)
    tg.addedge(30, 80)
    tg.addedge(40, 10)
    tg.addedge(20, 30)
    tg.addedge(50, 70)
    tg.addedge(10, 20)
    tg.addedge(60, 20)
    tg.addedge(60, 30)
    tg.addedge(70, 50)
    tg.addedge(30, 60)

    # Display Graph data
    print("Display Graph data")
    tg.Display()

    print()

    print("OUTPUT of 'for d in tg:'")
    for d in tg:
        print(d)
    print()

main()