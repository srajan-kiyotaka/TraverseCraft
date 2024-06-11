import unittest
from tkinter import Tk
from unittest.mock import patch
from traverseCraft.world import CreateTreeWorld
from traverseCraft.agent import TreeAgent

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

    def test_successful_initialization(self):
        treeWorld = CreateTreeWorld("Tree World Test", self.treeWorldInfo)
        self.assertEqual(treeWorld._worldName, "Tree World Test")
        self.assertEqual(treeWorld._treeRootId, 'A')
        self.assertEqual(treeWorld._goalIds, ['G'])
        self.assertEqual(treeWorld._position, self.treeWorldInfo['position'])
        self.assertIsInstance(treeWorld._root, Tk)
        self.assertIsNotNone(treeWorld.root)
        
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

    def test_invalid_tree_format(self):
        invalidInfo = self.treeWorldInfo.copy()
        invalidInfo['adj']['A'] = ['X']  # 'X' does not exist in position keys
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

    def test_custom_parameters(self):
        treeWorld = CreateTreeWorld(
            "Custom Tree World", self.treeWorldInfo, radius=25, fontSize=14, fontBold=False, 
            fontItalic=False, nodeColor="blue", rootColor="yellow", goalColor="orange", 
            width=800, height=600, lineThickness=3, arrowShape=(5, 10, 3), buttonBgColor="black", 
            buttonFgColor="white", textFont="Arial", textSize=18, textWeight="normal", buttonText="Run", 
            logoPath="custom_logo.png"
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
        self.assertEqual(treeWorld._logoPath, "custom_logo.png")

if __name__ == '__main__':
    unittest.main()