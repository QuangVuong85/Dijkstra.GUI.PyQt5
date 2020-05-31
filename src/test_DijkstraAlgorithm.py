import unittest
from DijkstraAlgorithm import Graph

class DijkstraAlgorithmTestCase(unittest.TestCase):
    def test(self):
        edges_dig = [
            ("A", "B", 7),
            ("A", "D", 5),
            ("B", "C", 8),
            ("B", "D", 9),
            ("B", "E", 7),
            ("C", "E", 5),
            ("D", "E", 15),
            ("D", "F", 6),
            ("E", "F", 8),
            ("E", "G", 9),
            ("F", "G", 11)
        ]

        edges_numb = [
            ('a', 'f', 14),
            ('a', 'c', 9),
            ('a', 'b', 7),
            ('c', 'd', 11),
            ('c', 'f', 2),
            ('c', 'a', 9),
            ('c', 'b', 10),
            ('b', 'd', 15),
            ('b', 'a', 7),
            ('b', 'c', 10),
            ('e', 'd', 6),
            ('e', 'f', 9),
            ('d', 'c', 11),
            ('d', 'e', 6),
            ('d', 'b', 15),
            ('f', 'a', 14),
            ('f', 'c', 2),
            ('f', 'e', 9)
        ]

        edges_numb1 = [
            (0, 1, 7),
            (0, 3, 5),
            (1, 2, 8),
            (1, 3, 9),
            (1, 4, 7),
            (2, 4, 5),
            (3, 4, 15),
            (3, 5, 6),
            (4, 5, 8),
            (4, 6, 9),
            (5, 6, 11)
        ]

        g = Graph(edges_dig, "A", "E")
        self.assertEqual(g.dijkstra(), (14, ['A', 'B', 'E']), msg="Path Should be (14, ['A', 'B', 'E'])")

        g = Graph(edges_numb, 'a', 'e')
        self.assertEqual(g.dijkstra(), (20, ['a', 'c', 'f', 'e']), msg="Path Should be (20, ['a', 'c', 'f', 'e'])")

        g = Graph(edges_numb1, 2, 3)
        self.assertEqual(g.dijkstra(), (float('inf'), []), msg="Path Should not be (inf, [])")


if __name__ == '__main__':
    unittest.main()