import unittest

from graph.Graph import Graph

class TestGraph(unittest.TestCase):
    def test_add_vertex_existing(self):
        sut = Graph()
        self.assertTrue(sut.add_vertex('A'))
        self.assertFalse(sut.add_vertex('A'))

    def test_add_edge(self):
        sut = Graph()
        sut.add_vertex('A')
        sut.add_vertex('B')
        self.assertTrue(sut.add_edge('A', 'B'))

    def test_add_edge_missing_vertex(self):
        sut = Graph()
        sut.add_vertex('A')
        self.assertFalse(sut.add_edge('A', 'B'))
