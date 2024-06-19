import unittest
from tkinter import Tk
from unittest.mock import patch
from src.traverseCraft.world import CreateTreeWorld
from src.traverseCraft.agent import TreeAgent
from src.traverseCraft.dataStructures import TreeNode 

class TestTreeAgent(unittest.TestCase):
    def setUp(self):
        # Sample tree world information
        treeWorldInfo = {
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
        # Create the tree world
        self.treeWorld = CreateTreeWorld("Tree World Test", treeWorldInfo)
        # Construct the world
        self.treeWorld.constructWorld()
        # Initialize the tree agent
        self.agent = TreeAgent(agentName="Test Tree Agent", world=self.treeWorld, heatMapColor="#EF4040")
        # Link the agent with the world
        self.treeWorld.setAgent(self.agent)

    def tearDown(self):
        # Destroy the root window after each test
        try:
            self.treeWorld._root.destroy()
            self.agent = None
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_initialization(self):
        # Test initialization of the tree agent
        self.assertIsInstance(self.agent._worldObj, CreateTreeWorld)
        self.assertEqual(self.agent._agentName, "Test Tree Agent")
        self.assertEqual(self.agent._agentColor, "blue")  # Default value
        self.assertTrue(self.agent._heatMapView)  # Default value
        self.assertEqual(self.agent._heatMapColor, "#EF4040")
        self.assertEqual(self.agent._heatGradient, 0.05)  # Default value
        self.assertIsNone(self.agent.algorithmCallBack)
        self.assertIsNotNone(self.agent._currentNode)

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
        self.assertTrue(True)

    def test_check_goal_state(self):
        # Check goal state
        self.assertFalse(self.agent.checkGoalState(self.agent._treeRoot.id))  # The root node should be a goal state
        self.assertTrue(self.agent.checkGoalState("G"))  # The node 'G' should be a goal state

    def test_move_agent(self):
        # Move the agent
        self.assertFalse(self.agent.moveAgent(None))  # Move to None should fail
        self.assertTrue(self.agent.moveAgent("B"))  # Move to node 'B' should succeed
        self.assertTrue(self.agent.moveAgent("C"))  # Move to node 'C' should succeed
        self.assertTrue(self.agent.moveAgent("D"))  # Move to node 'D' should succeed
        self.assertTrue(self.agent.moveAgent("E"))  # Move to node 'E' should succeed

if __name__ == '__main__':
    unittest.main()