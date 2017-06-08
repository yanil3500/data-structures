
"""
Tests for Graph
"""
import pytest

# I'm assuming that our depth first traversal algorithm is NOT going to visit same place twice
# Ex: 'Edges that begin at different vertices but end the same vertex'
# If there is an edge from H -> G, and there is an edge from C -> G, omit the second instance of same vertex from the list
# of vertices that have been visitied
PARAMETERS_FOR_TEST_DEPTH_FIRST_TRAVERSAL = [
    ([('A', 'B'), ('A', 'C'), ('B', 'H'), ('B', 'I'), ('H', 'G'), ('C', 'F'), ('C', 'G')], 'A', ['A', 'B', 'H', 'G', 'I', 'C', 'F']),
    ([(1, 7), (1, 8), (7, -10), (7, 5), (-10, 3), (3, 23), (3, -2), (-2, 57)], 1, [1, 7, -10, 3, 23, -2, 57, 5, 8]),
    ([('dan', 'jeff'), ('dan', 'brad'), ('brad', 'vinnie'), ('alex', 'dan'), ('alex', 'vinnie'), ('vinnie', 'tom'), ('vinnie', 'dog'), ('dog', 'clive'), ('dog', 'alex')], 'dan', ['dan', 'jeff', 'brad', 'vinnie', 'tom', 'dog', 'clive', 'alex']),
    ([('G', 'F'), ('F', 'E'), ('F', 7), (7, 8)], 8, []),
    ([('G', 89), (89, 1), (89, 2), (2, 1)], 'G', ['G', 89, 1, 2]),
    ([('G', 89), (89, 1), (89, 2), (2, 1)], 2, [2, 1])
]

PARAMETERS_FOR_TEST_BREADTH_FIRST_TRAVERSAL = [
    ([('A', 'B'), ('A' 'C'), ('B', 'H'), ('B', 'I'), ('H', 'G'), ('C', 'F'), ('C', 'G')], 'A', ['A', 'B', 'C', 'H', 'I', 'F', 'G']),
    ([(1, 7), (1, 8), (7, -10), (7, 5), (-10, 3), (3, 23), (3, -2), (-2, 57)], 1, [1, 7, 8, -10, 5, 3, 23, -2, 57]),
    ([('dan', 'jeff'), ('jeff', 'alex'), ('dan', 'brad'), ('brad', 'vinnie'), ('alex', 'dan'), ('alex', 'vinnie'), ('vinnie', 'tom'), ('vinnie', 'dog'), ('dog', 'clive'), ('dog', 'alex')], 'dan', ['dan', 'jeff', 'brad', 'alex', 'vinnie', 'tom', 'dog', 'clive']),
    ([('G', 89), (89, 1), (89, 2), (2, 1)], 'G', ['G', 89, 1, 2]),
    ([('G', 89), (89, 1), (89, 2), (2, 1)], 2, [2, 1])
]


NODES_TABLE = [
    [1, 2, 3, 4, 5, 6],
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['some string', 5, 'some other string', 99, 'yet another string']
]


EDGES_TABLE = [
    ([('A', 'B'), ('A', 'C'), ('B','D'), ('B', 'E'), ('C', 'F')], [('A', ['B', 'C']), ('B', ['D', 'E']), ('C', ['F'])]),
    ([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')], [('A', ['B']), ('B', ['C']), ('C', ['D']), ('D', ['E']), ('E', ['F']), ('F', ['A'])])
]


ADD_NODE_TABLE = [
    (['A', 'B', 'C', 'D', 'E', 'F']),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
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
    """
    a fixture for a binary tree graph
    """
    from graph import Graph
    graph = Graph()
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_node(letter)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')

    return graph


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


@pytest.mark.parametrize('nodes_to_add', ADD_NODE_TABLE)
def test_add_node(nodes_to_add):
    """Tests if we add nodes to graph correctly."""
    from graph import Graph
    graph = Graph()

    for node in nodes_to_add:
        graph.add_node(node)

    assert graph.nodes() == nodes_to_add


def test_del_node_with_no_nodes(empty_graph):
    """Tests if del_node method handles empty graph correctly."""
    from graph import Graph
    with pytest.raises(KeyError):
        empty_graph.del_node('A')


def test_del_node_with_no_edges(graph_with_no_edges):
    """Tests if we can delete nodes from graph with no edges."""
    from graph import Graph
    graph_with_no_edges.del_node('A')
    assert graph_with_no_edges.nodes() == ['B', 'C', 'D', 'E', 'F']


def test_del_nodes_with_edges(binary_tree_graph):
    """Test if we can delete nodes from a graph with edges. """
    from graph import Graph
    binary_tree_graph.del_node('C')
    assert binary_tree_graph.nodes() == ['A', 'B', 'D', 'E', 'F']


@pytest.mark.parametrize('vertices, start_val, result', PARAMETERS_FOR_TEST_DEPTH_FIRST_TRAVERSAL)
def test_depth_first_traveral(vertices, start_val, result, empty_graph):
    """
    This function asserts that the method returns a list of vertices visited in DFS order
    """
    for vertex_to_vertex in vertices:
        empty_graph.add_edge(vertex_to_vertex[0], vertex_to_vertex[1])
    assert empty_graph.depth_first_traversal(start_val) == result


@pytest.mark.parametrize('vertices, start_val, result', PARAMETERS_FOR_TEST_BREADTH_FIRST_TRAVERSAL)
def test_breadth_first_traversal(vertices, start_val, result):
    """
    This function asserts that the method returns a list of vertices visited in DFS order
    """
    for vertex_to_vertex in vertices:
        empty_graph.add_edge(vertex_to_vertex[0], vertex_to_vertex[1])
    assert empty_graph.breadth_first_traversal(start_val) == result


