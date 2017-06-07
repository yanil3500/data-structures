"""Test for Graph module."""

import pytest


NODES_TABLE = [
    [1, 2, 3, 4, 5, 6],
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['some string', 5, 'some other string', 99, 'yet another string']
]


EDGES_TABLE = [
    ([('A', 'B'), ('A', 'C'), ('B','D'), ('B', 'E'), ('C', 'F')], [('A', ['B', 'C']), ('B', ['D', 'E']), ('C', ['F'])]),
    ([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')], [('A', ['B']), ('B', ['C']), ('C', ['D']), ('D', ['E']), ('E', ['F']), ('F', ['A'])])
]


@pytest.fixture
def empty_graph():
    from graph import Graph
    return Graph()


@pytest.fixture
def graph_with_no_edges():
    from graph import Graph
    graph = Graph()
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_node(letter)

    return graph


@pytest.fixture
def binary_tree_graph():
    from graph import Graph
    graph = Graph()
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_node(letter)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')


############### TESTS #######################


def test_init(empty_graph):
    """Test init method."""
    assert empty_graph.graph_dict == {}


@pytest.mark.parametrize('nodes', NODES_TABLE)
def test_nodes(nodes):
    """Test nodes method."""
    from graph import Graph
    graph = Graph()
    for node in nodes:
        graph.add_node(node)

    assert graph.nodes() == nodes


@pytest.mark.parametrize('nodes', NODES_TABLE)
def test_has_node(nodes):
    """Test has_nodes method."""
    from graph import Graph
    graph = Graph()
    for node in nodes:
        graph.add_node(node)

    for node in nodes:
        assert graph.has_node(node)


@pytest.mark.parametrize('edges, edges_output', EDGES_TABLE)
def test_edges(edges, edges_output):
    """Tests if we have correct set of edges."""
    from graph import Graph
    graph = Graph()

    for set_of_edges in edges:
        graph.add_edge(set_of_edges[0], set_of_edges[1])

    assert graph.edges() == edges_output

