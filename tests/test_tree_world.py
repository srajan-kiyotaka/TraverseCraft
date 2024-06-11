import unittest
from tkinter import Tk
from unittest.mock import patch
from traverseCraft.world import CreateTreeWorld
from traverseCraft.agent import TreeAgent
from traverseCraft.dataStructures import TreeNode 

class TestTreeWorld(unittest.TestCase):

    def setUp(self):
        # Sample valid tree information
        self.treeWorldInfo = {
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
                'G': (400, 400),
                'H': (150, 400)
            },
            'root': 'A',
            'goals': ['G']
        }

    # def tearDown(self):
    #     try:
    #         self.grid_world._root.destroy()
    #     except Exception as e:
    #         print(f"Exception in tearDown: {e}")

    def test_successful_initialization(self):
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)
        self.assertEqual(treeWorld._worldName, "Tree World Test")
        self.assertEqual(treeWorld._treeRootId, 'A')
        self.assertEqual(treeWorld._goalIds, ['G'])
        self.assertEqual(treeWorld._position, self.treeWorldInfo['position'])
        self.assertIsInstance(treeWorld._root, Tk)
        self.assertIsNotNone(treeWorld.root)
        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")
        
    def test_missing_root_key(self):
        invalidInfo = self.treeWorldInfo.copy()
        del invalidInfo['root']
        with self.assertRaises(ValueError):
            CreateTreeWorld("Tree World Test", invalidInfo)
            
    def test_missing_goals_key(self):
        invalidInfo = self.treeWorldInfo.copy()
        del invalidInfo['goals']
        with self.assertRaises(ValueError):
            CreateTreeWorld("Tree World Test", invalidInfo)

    def test_missing_adj_key(self):
        invalidInfo = self.treeWorldInfo.copy()
        del invalidInfo['adj']
        with self.assertRaises(ValueError):
            CreateTreeWorld("Tree World Test", invalidInfo)

    def test_missing_position_key(self):
        invalidInfo = self.treeWorldInfo.copy()
        del invalidInfo['position']
        with self.assertRaises(ValueError):
            CreateTreeWorld("Tree World Test", invalidInfo)

    def test_default_parameters(self):
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)
        self.assertEqual(treeWorld._radius, 20)
        self.assertEqual(treeWorld._fontSize, 12)
        self.assertEqual(treeWorld._fontBold, True)
        self.assertEqual(treeWorld._fontItalic, True)
        self.assertEqual(treeWorld._nodeColor, "gray")
        self.assertEqual(treeWorld._rootColor, "red")
        self.assertEqual(treeWorld._goalColor, "green")
        self.assertEqual(treeWorld._lineThickness, 2)
        self.assertEqual(treeWorld._arrowShape, (10, 12, 5))
        self.assertEqual(treeWorld._buttonBgColor, "#7FC7D9")
        self.assertEqual(treeWorld._buttonFgColor, "#332941")
        self.assertEqual(treeWorld._textFont, "Helvetica")
        self.assertEqual(treeWorld._textSize, 24)
        self.assertEqual(treeWorld._textWeight, "bold")
        self.assertEqual(treeWorld._buttonText, "Start Agent")
        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_custom_parameters(self):
        treeWorld = CreateTreeWorld(
            "Custom Tree World", self.treeWorldInfo, radius=25, fontSize=14, fontBold=False, 
            fontItalic=False, nodeColor="blue", rootColor="yellow", goalColor="orange", 
            width=800, height=600, lineThickness=3, arrowShape=(5, 10, 3), buttonBgColor="black", 
            buttonFgColor="white", textFont="Arial", textSize=18, textWeight="normal", buttonText="Run"
        )
        self.assertEqual(treeWorld._radius, 25)
        self.assertEqual(treeWorld._fontSize, 14)
        self.assertEqual(treeWorld._fontBold, False)
        self.assertEqual(treeWorld._fontItalic, False)
        self.assertEqual(treeWorld._nodeColor, "blue")
        self.assertEqual(treeWorld._rootColor, "yellow")
        self.assertEqual(treeWorld._goalColor, "orange")
        self.assertEqual(treeWorld._width, 800)
        self.assertEqual(treeWorld._height, 600)
        self.assertEqual(treeWorld._lineThickness, 3)
        self.assertEqual(treeWorld._arrowShape, (5, 10, 3))
        self.assertEqual(treeWorld._buttonBgColor, "black")
        self.assertEqual(treeWorld._buttonFgColor, "white")
        self.assertEqual(treeWorld._textFont, "Arial")
        self.assertEqual(treeWorld._textSize, 18)
        self.assertEqual(treeWorld._textWeight, "normal")
        self.assertEqual(treeWorld._buttonText, "Run")
        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_valid_tree_format(self):
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)
        self.assertTrue(treeWorld._check_tree_format(self.treeWorldInfo)[0])
        try:
            treeWorld._root.destroy()
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
            'root': 'A',
            'goals': ['G']
        }
        for info in missing_keys:
            with self.assertRaises(ValueError):
                CreateTreeWorld("Tree World Test", info)


    def test_invalid_node_coordinates(self):
        invalid_coords = [
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, '100'), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100,), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']}
        ]
        for info in invalid_coords:
            with self.assertRaises(ValueError):
                CreateTreeWorld("Tree World Test", info)

    def test_invalid_goal_nodes(self):
        invalid_goals = [
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A','goals': ['D']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A','goals': [1]}
        ]
        for info in invalid_goals:
            with self.assertRaises(ValueError):
                CreateTreeWorld("Tree World Test", info)

    def test_missing_nodes(self):
        missing_nodes = [
            {'adj': {'A': ['B'], 'B': ['C'], 'D': []}, 'position': {'A': (0, 0), 'B': (100, 100), 'C': (200, 200)}, 'root': 'A', 'goals': ['C']},
            {'adj': {'A': ['B'], 'B': ['C'], 'C': []}, 'position': {'A': (0, 0), 'B': (100, 100)}, 'root': 'A', 'goals': ['C']}
        ]
        for info in missing_nodes:
            with self.assertRaises(ValueError):
                CreateTreeWorld("Tree World Test", info)

    def test_node_map_pointers(self):
        # Create the tree world
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)

        # Assert that all values in nodeMap are instances of TreeNode class
        for node_id, node_obj in treeWorld.nodeMap.items():
            self.assertIsInstance(node_obj, TreeNode)
        
        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")
        

    def test_get_node(self):
        # Create the tree world
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)

        # Test getNode method
        node_A = treeWorld.getNode('A')
        node_B = treeWorld.getNode('B')
        node_C = treeWorld.getNode('C')

        # Assert nodes are retrieved correctly
        self.assertEqual(node_A.id, 'A')
        self.assertEqual(node_B.id, 'B')
        self.assertEqual(node_C.id, 'C')

        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    @patch.object(Tk, 'mainloop', lambda self: None)
    def test_show_world(self):
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)

        # Test showWorld method
        treeWorld.showWorld()

        # Verify that the _root window is initialized after calling showWorld
        self.assertIsInstance(treeWorld._root, Tk)

        # Verify that the _root window is visible
        self.assertTrue(treeWorld._root.winfo_exists())

        try:
            treeWorld._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")


if __name__ == '__main__':
    unittest.main()