# `TreeAgent` Class API Reference

## Class: `TreeAgent`
The `TreeAgent` class represents an agent that operates within a tree-structured environment. The agent can traverse the tree, track its movement, and visualize its path using a heat map.

### Parameters
- **world** (`CreateTreeWorld`): The world object that the agent belongs to.
- **agentName** (`str`): The name of the agent.
- **agentColor** (`str`, optional): The color of the agent. Defaults to "blue".
- **heatMapView** (`bool`, optional): Flag indicating whether to enable heat map view. Defaults to True.
- **heatMapColor** (`str`, optional): The color of the heat map. Defaults to "#FFA732".
- **heatGradient** (`float`, optional): The gradient of the heat map. Defaults to 0.05.

### Attributes
- **algorithmCallBack** (`function`): Callback function for the agent's algorithm.

### Public Methods

#### `__init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", heatGradient:float=0.05)`
The constructor initializes a new instance of the `TreeAgent` class. It sets up the agent within the given tree world and initializes various attributes such as agent name, color, heat map settings, and the starting position in the tree.


- **Parameters**:
  - `world` (`CreateTreeWorld`): The tree world object.
  - `agentName` (`str`): The name of the agent.
  - `agentColor` (`str`, optional): The color of the agent. Defaults to "blue".
  - `heatMapView` (`bool`, optional): Whether to enable the heat map view. Defaults to True.
  - `heatMapColor` (`str`, optional): The color of the heat map. Defaults to "#FFA732".
  - `heatGradient` (`float`, optional): The gradient value for the heat map. Defaults to 0.05.

#### `__str__(self)`
This method provides a string representation of the agent, calling the `aboutAgent` method internally.

- **Returns**: 
  - `str`: A string containing information about the agent.

#### `aboutAgent(self)`
This method returns a detailed description of the agent's attributes, such as agent name, color, world name, world ID, and root node ID, formatted in a table for readability.

- **Returns**:
  - `str`: A string containing information about the agent, including agent name, color, world name, world ID, and root node ID.

#### `summary(self)`
This method provides a summary of the agent's run, including the start time, end time, and the elapsed time of the run. This information is formatted in a table for clarity.

- **Returns**:
  - `str`: A summary of the agent's run, including start time, end time, and elapsed time.

#### `setAlgorithmCallBack(self, algorithmCallBack)`
This method sets the callback function that will be executed by the agent. The callback function defines the algorithm the agent will follow while traversing the tree.

- **Parameters**:
  - `algorithmCallBack` (`function`): The callback function to be set.

- **Returns**:
  - `None`

#### `runAlgorithm(self)`
This method executes the previously set algorithm callback function. It also sets the start time before execution and the end time after execution to track the algorithm's runtime.

- **Raises**:
  - `ValueError`: If the algorithm callback function is not set.

#### `getHeatMapColor(self, value: float)`
This method returns the color corresponding to a given value on a heat map. It uses an exponential decay function to map the value to a color, which helps visualize the heat map effectively.

- **Parameters**:
  - `value` (`float`): The value to map to a color on the heat map.

- **Returns**:
  - `tuple`: The RGB color value for the given value on the heat map.

#### `checkGoalState(self, node)`
This method checks if the specified node is a goal state.

- **Parameters**:
  - `node` (`TreeNode`): The node to be checked.

- **Returns**:
  - `bool`: True if the node is a goal state, False otherwise.

#### `moveAgent(self, node, delay:int=1)`
This method moves the agent to the specified node after a given delay. It updates the heat map and the agent's current position.

- **Parameters**:
  - `node` (`TreeNode`): The node to which the agent should be moved.
  - `delay` (`int`, optional): The delay (in seconds) before moving to the next node. Defaults to 1 second.

- **Returns**:
  - `bool`: True if the agent was successfully moved to the node, False otherwise.
