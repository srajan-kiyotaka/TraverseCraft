import unittest
from tkinter import Tk
from unittest.mock import patch
from src.traverseCraft.world import CreateGraphWorld
from src.traverseCraft.agent import GraphAgent
from src.traverseCraft.dataStructures import GraphNode 

class TestGraphAgent(unittest.TestCase):
    def setUp(self):
        # Sample Graph world information
        graphWorldInfo = {
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
        # Create the Graph world
        self.graphWorld = CreateGraphWorld("Graph World Test", graphWorldInfo)

        # Construct the world
        self.graphWorld.constructWorld()

        # Initialize the Graph agent
        self.agent = GraphAgent(agentName="Test Graph Agent", world=self.graphWorld, heatMapColor="#EF4040")

        # Link the agent with the world
        self.graphWorld.setAgent(self.agent)

    def tearDown(self):
        # Destroy the root window after each test
        try:
            self.graphWorld._root.destroy()
            self.agent = None
        except Exception as e:
            print(f"Exception in tearDown: {e}")

    def test_initialization(self):
        # Test initialization of the Graph agent
        self.assertEqual(self.agent._worldObj, self.graphWorld)
        self.assertEqual(self.agent._worldID, "GRAPHWORLD")
        self.assertEqual(self.agent._agentName, "Test Graph Agent")
        self.assertEqual(self.agent._agentColor, "blue")
        self.assertTrue(self.agent._heatMapView)
        self.assertNotEqual(self.agent._heatMapColor, "#FFA732")
        self.assertEqual(self.agent._heatGradient, 0.05)

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
        self.assertTrue(self.agent.checkGoalState("G"))
        self.assertFalse(self.agent.checkGoalState("A"))

    def test_set_start_state(self):
        self.agent.setStartState("B")
        self.assertEqual(self.agent._currentNode.id, "B")
        self.assertEqual(self.agent._graphRoot.id, "B")
        self.assertEqual(self.graphWorld.root.id, "B")

    def test_set_start_state_invalid(self):
        with self.assertRaises(ValueError):
            self.agent.setStartState("Z")  # Assuming "Z" is not a valid node ID
    
    def test_move_agent(self):
        # Move the agent
        self.assertFalse(self.agent.moveAgent(None))  # Move to None should fail
        self.assertTrue(self.agent.moveAgent("B"))  # Move to node 'B' should succeed
        self.assertTrue(self.agent.moveAgent("C"))  # Move to node 'C' should succeed
        self.assertTrue(self.agent.moveAgent("D"))  # Move to node 'D' should succeed
        self.assertTrue(self.agent.moveAgent("E"))  # Move to node 'E' should succeed

if __name__ == '__main__':
    unittest.main()
