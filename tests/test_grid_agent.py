import unittest
from tkinter import Tk
from unittest.mock import patch
from traverseCraft.world import CreateGridWorld
from traverseCraft.agent import GridAgent

class TestGridAgent(unittest.TestCase):
    def setUp(self):
        # Setup code to initialize the grid world
        self.grid_world = CreateGridWorld(worldName='Test Grid', rows=10, cols=10, cellSize=20, pathColor="black", blockColor="pink", goalColor="aqua", cellPadding=4, borderWidth=2, buttonBgColor="#7FC8D9", buttonFgColor="#332942", textFont="Helvetica", textSize=20, textWeight="bold", buttonText="Test Start Agent", logoPath=None)
        
        # Set goal state
        self.grid_world.addGoalState([[5, 5], [6, 9], [8, 8]])

        # Set block state
        self.grid_world.addBlockPath([[1, 1], [2, 2], [3, 3], [2, 7], [8, 5], [6, 1]])

        # Construct the grid world
        self.grid_world.constructWorld()

        # Initialize the grid agent
        self.agent = GridAgent(self.grid_world, agentName='TestAgent', agentColor='blue', heatMapView=True, heatMapColor='#FFA732', agentPos=(0, 0), heatGradient=0.05)

    def tearDown(self):
        # Destroy the root window after each test
        self.grid_world._root.destroy()

    def test_initialization(self):
        # Test initialization of the grid agent
        self.assertIsInstance(self.agent._worldObj, CreateGridWorld)
        self.assertEqual(self.agent._agentName, 'TestAgent')
        self.assertEqual(self.agent._agentColor, 'blue')
        self.assertTrue(self.agent._heatMapView)
        self.assertEqual(self.agent._heatMapColor, '#FFA732')
        self.assertEqual(self.agent._heatGradient, 0.05)
        self.assertEqual(self.agent._startState, (0, 0))
        self.assertEqual(self.agent._currentPosition, (0, 0))
        self.assertIsNone(self.agent.algorithmCallBack)

    def test_initial_start_state(self):
        # Test initial start state
        self.assertEqual(self.agent._startState, (0, 0))
        self.assertEqual(self.agent._currentPosition, (0, 0))


    def test_set_start_state(self):
        # Update start state
        self.agent.setStartState(1, 8)

        # Verify updated start state
        self.assertEqual(self.agent._startState, (1, 8))
        self.assertEqual(self.agent._currentPosition, (1, 8))
        self.assertEqual(self.grid_world._cells[1][8].cget("bg"), 'blue')  # Check if cell color updated
        self.assertEqual(self.grid_world._cells[0][0].cget("bg"), 'black')  # Check previous cell color


        # Update start state again
        self.agent.setStartState(3, 6)

        # Verify updated start state
        self.assertEqual(self.agent._startState, (3, 6))
        self.assertEqual(self.agent._currentPosition, (3, 6))
        self.assertEqual(self.grid_world._cells[3][6].cget("bg"), 'blue')  # Check if cell color updated
        self.assertEqual(self.grid_world._cells[1][8].cget("bg"), 'black')  # Check previous cell color


    def test_invalid_start_state(self):
        # Test setting an invalid start state
        with self.assertRaises(ValueError):
            self.agent.setStartState(20, 20)  # Invalid position, should raise ValueError

        # Verify that start state remains unchanged
        self.assertEqual(self.agent._startState, (0, 0))
        self.assertEqual(self.agent._currentPosition, (0, 0))


    def test_check_goal_state(self):
              
        # Check goal states
        self.assertTrue(self.agent.checkGoalState(5, 5))  # Should return True
        self.assertTrue(self.agent.checkGoalState(6, 9))  # Should return True
        self.assertTrue(self.agent.checkGoalState(8, 8))  # Should return True
        self.assertFalse(self.agent.checkGoalState(0, 0))  # Should return False

    def test_check_block_state(self):
        # Check block states
        self.assertTrue(self.agent.checkBlockState(1, 1))  # Should return True
        self.assertTrue(self.agent.checkBlockState(2, 2))  # Should return True
        self.assertTrue(self.agent.checkBlockState(3, 3))  # Should return True
        self.assertTrue(self.agent.checkBlockState(2, 7))  # Should return True
        self.assertTrue(self.agent.checkBlockState(8, 5))  # Should return True
        self.assertTrue(self.agent.checkBlockState(6, 1))  # Should return True
        self.assertFalse(self.agent.checkBlockState(0, 0))  # Should return False

    def test_set_algorithm_callback(self):
        # Define a sample callback function
        def sample_callback():
            pass

        # Set the callback function
        self.agent.setAlgorithmCallBack(sample_callback)
        
        # Verify that the callback function is set
        self.assertEqual(self.agent.algorithmCallBack, sample_callback)

    def test_run_algorithm(self):
        # Define a sample algorithm callback function
        def sample_algorithm():
            pass

        # Set the algorithm callback function
        self.agent.setAlgorithmCallBack(sample_algorithm)
        
        # Run the algorithm
        self.agent.runAlgorithm()
        
        # Verify that the algorithm ran successfully (no errors raised)

    def test_move_agent(self):
        # Define a sample algorithm callback function
        def sample_algorithm():
            pass

        # Set the algorithm callback function
        self.agent.setAlgorithmCallBack(sample_algorithm)
        
        # Run the algorithm
        self.agent.runAlgorithm()

        # Move the agent
        self.assertTrue(self.agent.moveAgent(1, 0))  # Should return True
        self.assertEqual(self.agent._currentPosition, (1, 0))  # Verify agent's current position
        self.assertTrue(self.agent.moveAgent(0, 3))  # Should return True
        self.assertEqual(self.agent._currentPosition, (0, 3))  # Verify agent's current position


if __name__ == '__main__':
    unittest.main()