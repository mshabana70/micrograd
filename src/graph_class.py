from graphviz import Digraph
from value import Value

def trace(root):
    # builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    
    build(root)
    return nodes, edges

def draw_dot(root):

    dot = Digraph(format='png', graph_attr={'rankdir': 'LR'}) # LR = left to right

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))

        # for any value in the graph, create a rectangular ('record') node for it
        dot.node(name = uid, label = "{ data %.4f }" % (n.data, ), shape='record')

        if n._op:
            # if the value has an operation, create a circular node for it
            dot.node(name = uid + 'op', label = n._op, shape='circle')
            # create an edge from the operation to the value
            dot.edge(uid + 'op', uid)
    
    for n1, n2 in edges:
        # Connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot


def main():

    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    d = a * b + c

    draw_dot(d).render('img/complex_graph.gv', view=True)

if __name__ == "__main__":
    main()