import unittest
from tkinter import Tk
from unittest.mock import patch
from src.traverseCraft.world import CreateGridWorld
from src.traverseCraft.agent import GridAgent

class TestGridWorld(unittest.TestCase):
    def setUp(self):
        # Setup code to initialize the grid world
        self.grid_world = CreateGridWorld(worldName='Test Grid', rows=10, cols=10, cellSize=20, pathColor="black", blockColor="pink", goalColor="aqua", cellPadding=4, borderWidth=2, buttonBgColor="#7FC8D9", buttonFgColor="#332942", textFont="Helvetica", textSize=20, textWeight="bold", buttonText="Test Start Agent", logoPath=None)


    def tearDown(self):
        try:
            self.grid_world._root.destroy()
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_initial_state(self):
        # Test the initial state of the grid world
        self.assertEqual(self.grid_world._worldName, 'Test Grid')
        self.assertEqual(self.grid_world._rows, 10)
        self.assertEqual(self.grid_world._cols, 10)
        self.assertEqual(self.grid_world._cellSize, 20)
        self.assertEqual(self.grid_world._pathColor, "black")
        self.assertEqual(self.grid_world._blockColor, "pink")
        self.assertEqual(self.grid_world._goalColor, "aqua")
        self.assertEqual(self.grid_world._cellPadding, 4)
        self.assertEqual(self.grid_world._borderWidth, 2)
        self.assertEqual(self.grid_world._buttonBgColor, "#7FC8D9")
        self.assertEqual(self.grid_world._buttonFgColor, "#332942")
        self.assertEqual(self.grid_world._textFont, "Helvetica")
        self.assertEqual(self.grid_world._textSize, 20)
        self.assertEqual(self.grid_world._textWeight, "bold")
        self.assertEqual(self.grid_world._buttonText, "Test Start Agent")
        self.assertIsNone(self.grid_world._agent)

    def test_heat_map_initialization(self):
        # Check if the heat map grid is initialized correctly
        expected_rows = 10
        expected_cols = 10

        self.assertEqual(len(self.grid_world._heatMapValueGrid), expected_rows, "Number of rows in heat map grid is incorrect.")
        for row in self.grid_world._heatMapValueGrid:
            self.assertEqual(len(row), expected_cols, "Number of columns in heat map grid is incorrect.")
            self.assertTrue(all(value == 0 for value in row), "Initial heat map values should be 0.")

    def test_cells_not_none_and_bound(self):
        # Define the block path to be added
        block_path = [[1, 1], [2, 2], [3, 3], [2, 7], [8, 5], [6, 1]]
        
        # Add the block path to the grid world
        self.grid_world.setBlockPath(block_path)

        # Define the goal state to be added
        goal_state = [[5, 5], [6, 9], [8, 8]]
        
        # Add the goal state to the grid world
        self.grid_world.setGoalState(goal_state)

        # Construct the grid world
        self.grid_world.constructWorld()
        
        for i in range(self.grid_world._rows):
            for j in range(self.grid_world._cols):
                with self.subTest(i=i, j=j):
                    cell = self.grid_world._cells[i][j]
                    self.assertIsNotNone(cell, f"Cell ({i}, {j}) is None.")
                    
                    # Check if the cell is a goal cell
                    if [i, j] in self.grid_world._goalCells:
                        bindings = cell.bind()
                        self.assertNotIn("<Button-1>", bindings, f"Goal cell ({i}, {j}) should not have <Button-1> event bound.")
                    else:
                        bindings = cell.bind()
                        self.assertIn("<Button-1>", bindings, f"Cell ({i}, {j}) does not have <Button-1> event bound.")
    
    def test_add_block_path(self):
        # Define the block path to be added
        block_path = [[1, 1], [2, 2], [3, 3], [2, 7], [8, 5], [6, 1]]
        
        # Add the block path to the grid world
        self.grid_world.setBlockPath(block_path)
        
        # Verify that the cells corresponding to the block path are set correctly
        for coordinate in block_path:
            i, j = coordinate
            with self.subTest(i=i, j=j):
                cell = self.grid_world._cells[i][j]
                self.assertEqual(cell.cget("bg"), self.grid_world._blockColor, f"Cell ({i}, {j}) does not have block color.")
                self.assertEqual(self.grid_world._world[i][j], -1, f"Cell ({i}, {j}) is not marked as a block in the world grid.")
                
                # Check if the coordinate is present in _blockCells
                self.assertIn(coordinate, self.grid_world._blockCells, f"Coordinate {coordinate} is not present in _blockCells.")

    def test_add_goal_state(self):
        # Define the goal state to be added
        goal_state = [[5, 5], [6, 9], [8, 8]]
        
        # Add the goal state to the grid world
        self.grid_world.setGoalState(goal_state)
        
        # Verify that the cells corresponding to the goal state are set correctly
        for coordinate in goal_state:
            i, j = coordinate
            with self.subTest(i=i, j=j):
                cell = self.grid_world._cells[i][j]
                self.assertEqual(cell.cget("bg"), self.grid_world._goalColor, f"Cell ({i}, {j}) does not have goal color.")
                self.assertEqual(self.grid_world._world[i][j], 1, f"Cell ({i}, {j}) is not marked as a goal state in the world grid.")
                
                # Check if the coordinate is present in _goalCells
                self.assertIn(coordinate, self.grid_world._goalCells, f"Coordinate {coordinate} is not present in _goalCells.")


    @patch.object(Tk, 'mainloop', lambda self: None)
    def test_show_world(self):
        # Call the showWorld function
        self.grid_world.showWorld()

        # Verify that the _root window is initialized after calling showWorld
        self.assertIsInstance(self.grid_world._root, Tk)

        # Verify that the _root window is visible
        self.assertTrue(self.grid_world._root.winfo_exists())


if __name__ == '__main__':
    unittest.main()