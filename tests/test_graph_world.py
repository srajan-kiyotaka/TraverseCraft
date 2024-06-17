import unittest
from tkinter import Tk
from unittest.mock import patch
from src.traverseCraft.world import CreateGraphWorld
from src.traverseCraft.dataStructures import GraphNode 

class TestGraphWorld(unittest.TestCase):

    def setUp(self):
        # Sample valid Graph information
        self.graphWorldInfo = {
    'adj': {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['H', 'A'],
        'F': ['G'],
        'G': ['H', 'C'],
        'H': ['D', 'E']
    },
    'position': {
        'A': (300, 100),
        'B': (150, 200),
        'C': (450, 200),
        'D': (100, 300),
        'E': (200, 300),
        'F': (300, 300),
        'G': (400, 400),
        'H': (150, 400)

    },
    'goals': ['G']
}

    # def tearDown(self):
    #     try:
    #         self.grid_world._root.destroy()
    #     except Exception as e:
    #         print(f"Exception in tearDown: {e}")

    def test_successful_initialization(self):
        self.graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)
        self.assertEqual(self.graphWorld._worldName, "Graph World Test")
        self.assertEqual(self.graphWorld._goalIds, ['G'])
        self.assertEqual(self.graphWorld._position['A'], (300, 100))
        self.assertEqual(self.graphWorld._nodeColor, "gray")
        self.assertEqual(self.graphWorld._goalColor, "green")
        self.assertEqual(self.graphWorld._fontSize, 12)
        self.assertTrue(self.graphWorld._fontBold)
        self.assertTrue(self.graphWorld._fontItalic)
        self.assertEqual(self.graphWorld._lineThickness, 2)
        self.assertEqual(self.graphWorld._arrowShape, (10, 12, 5))
        self.assertEqual(self.graphWorld._buttonBgColor, "#7FC7D9")
        self.assertEqual(self.graphWorld._buttonFgColor, "#332941")
        self.assertEqual(self.graphWorld._textFont, "Helvetica")
        self.assertEqual(self.graphWorld._textSize, 24)
        self.assertEqual(self.graphWorld._textWeight, "bold")
        self.assertEqual(self.graphWorld._buttonText, "Start Agent")
        try:
            self.graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")
        
              
    def test_missing_goals_key(self):
        invalidInfo = self.graphWorldInfo.copy()
        del invalidInfo['goals']
        with self.assertRaises(ValueError):
            CreateGraphWorld("Graph World Test", invalidInfo)

    def test_missing_adj_key(self):
        invalidInfo = self.graphWorldInfo.copy()
        del invalidInfo['adj']
        with self.assertRaises(ValueError):
            CreateGraphWorld("Graph World Test", invalidInfo)

    def test_missing_position_key(self):
        invalidInfo = self.graphWorldInfo.copy()
        del invalidInfo['position']
        with self.assertRaises(ValueError):
            CreateGraphWorld("Graph World Test", invalidInfo)

    def test_default_parameters(self):
        graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)
        self.assertEqual(graphWorld._radius, 20)
        self.assertEqual(graphWorld._fontSize, 12)
        self.assertEqual(graphWorld._fontBold, True)
        self.assertEqual(graphWorld._fontItalic, True)
        self.assertEqual(graphWorld._nodeColor, "gray")
        self.assertEqual(graphWorld._goalColor, "green")
        self.assertEqual(graphWorld._lineThickness, 2)
        self.assertEqual(graphWorld._arrowShape, (10, 12, 5))
        self.assertEqual(graphWorld._buttonBgColor, "#7FC7D9")
        self.assertEqual(graphWorld._buttonFgColor, "#332941")
        self.assertEqual(graphWorld._textFont, "Helvetica")
        self.assertEqual(graphWorld._textSize, 24)
        self.assertEqual(graphWorld._textWeight, "bold")
        self.assertEqual(graphWorld._buttonText, "Start Agent")
        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_custom_parameters(self):
        graphWorld = CreateGraphWorld(
            "Custom Graph World", self.graphWorldInfo, radius=25, fontSize=14, fontBold=False, 
            fontItalic=False, nodeColor="blue", goalColor="orange", 
            width=800, height=600, lineThickness=3, arrowShape=(5, 10, 3), buttonBgColor="black", 
            buttonFgColor="white", textFont="Arial", textSize=18, textWeight="normal", buttonText="Run"
        )
        self.assertEqual(graphWorld._radius, 25)
        self.assertEqual(graphWorld._fontSize, 14)
        self.assertEqual(graphWorld._fontBold, False)
        self.assertEqual(graphWorld._fontItalic, False)
        self.assertEqual(graphWorld._nodeColor, "blue")
        self.assertEqual(graphWorld._goalColor, "orange")
        self.assertEqual(graphWorld._width, 800)
        self.assertEqual(graphWorld._height, 600)
        self.assertEqual(graphWorld._lineThickness, 3)
        self.assertEqual(graphWorld._arrowShape, (5, 10, 3))
        self.assertEqual(graphWorld._buttonBgColor, "black")
        self.assertEqual(graphWorld._buttonFgColor, "white")
        self.assertEqual(graphWorld._textFont, "Arial")
        self.assertEqual(graphWorld._textSize, 18)
        self.assertEqual(graphWorld._textWeight, "normal")
        self.assertEqual(graphWorld._buttonText, "Run")
        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_valid_graph_format(self):
        graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)
        self.assertTrue(graphWorld._check_graph_format(self.graphWorldInfo)[0])
        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_missing_keys(self):
        missing_keys = {
            'adj': {
                'A': ['B', 'C'],
                'B': ['D', 'E'],
                'C': ['F'],
                'D': [],
                'E': ['H'],
                'F': ['G'],
                'G': [],
                'H': []
            },
            'position': {
                'A': (300, 100),
                'B': (150, 200),
                'C': (450, 200),
                'D': (100, 300),
                'E': (200, 300),
                'F': (300, 300),
                'G': (400, 400)
            },
            'goals': ['G']
        }
        with self.assertRaises(ValueError):
            CreateGraphWorld("Graph World Test", missing_keys)


    def test_invalid_node_coordinates(self):
        invalid_coords = [
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, '100'), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100,), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']}
        ]
        for info in invalid_coords:
            with self.assertRaises(ValueError):
                CreateGraphWorld("Graph World Test", info)

    def test_invalid_goal_nodes(self):
        invalid_goals = [
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A','goals': ['D']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A','goals': [1]}
        ]
        for info in invalid_goals:
            with self.assertRaises(ValueError):
                CreateGraphWorld("Graph World Test", info)

    def test_missing_nodes(self):
        missing_nodes = [
            {'adj': {'A': ['B'], 'B': ['C'], 'D': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100)}, 'root': 'A', 'goals': ['C']}
        ]
        for info in missing_nodes:
            with self.assertRaises(ValueError):
                CreateGraphWorld("Graph World Test", info)

    def test_node_map_pointers(self):
        # Create the Graph world
        graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)

        # Assert that all values in nodeMap are instances of GraphNode class
        for node_id, node_obj in graphWorld.nodeMap.items():
            self.assertIsInstance(node_obj, GraphNode)
        
        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")
        

    def test_get_node(self):
        # Create the Graph world
        graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)

        # Test getNode method
        node_A = graphWorld.getNode('A')
        node_B = graphWorld.getNode('B')
        node_C = graphWorld.getNode('C')

        # Assert nodes are retrieved correctly
        self.assertEqual(node_A.id, 'A')
        self.assertEqual(node_B.id, 'B')
        self.assertEqual(node_C.id, 'C')

        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    @patch.object(Tk, 'mainloop', lambda self: None)
    def test_show_world(self):
        graphWorld = CreateGraphWorld("Graph World Test", self.graphWorldInfo)

        # Test showWorld method
        graphWorld.showWorld()

        # Verify that the _root window is initialized after calling showWorld
        self.assertIsInstance(graphWorld._root, Tk)

        # Verify that the _root window is visible
        self.assertTrue(graphWorld._root.winfo_exists())

        try:
            graphWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")


if __name__ == '__main__':
    unittest.main()