"""Test for Graph module."""

import pytest


NODES_TABLE = [
    [1, 2, 3, 4, 5, 6],
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['some string', 5, 'some other string', 99, 'yet another string']
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