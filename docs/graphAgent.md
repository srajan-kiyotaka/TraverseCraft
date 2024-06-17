# GraphAgent Class API Reference

The `GraphAgent` class represents an agent that operates within a graph world. This agent can move between nodes, execute algorithms, and update a heat map to visualize the agent's path.

## Parameters

- **Parameters**:
  - `world` (`CreateGraphWorld`): The graph world object that the agent belongs to.
  - `agentName` (`str`): The name of the agent.
  - `agentColor` (`str`, optional): The color of the agent. Defaults to "blue".
  - `startNodeId` (`str`, optional): The ID of the starting node. If not provided, the root node of the graph is used.
  - `heatMapView` (`bool`, optional): Flag indicating whether to enable heat map view. Defaults to True.
  - `heatMapColor` (`str`, optional): The color of the heat map. Defaults to "#FFA732".
  - `heatGradient` (`float`, optional): The gradient of the heat map. Defaults to 0.05.

## Methods

### `__str__(self)`

This method provides a string representation of the GraphAgent object. It returns a formatted string that summarizes important attributes of the agent, such as its name, color, world name, world ID, and the ID of the start node. This method is useful for quickly inspecting the current state of the agent.

- **Returns**:
  - `str`: A string containing information about the agent.

### `aboutAgent(self)`

The aboutAgent method generates and returns a detailed summary of the agent's attributes. It uses the PrettyTable library to create a structured table that displays key information about the agent, including its name, assigned color, the name and ID of the world it operates in, and the ID of the node where it currently resides. This summary is designed to provide a clear overview of the agent's setup and current state.

- **Returns**:
  - `str`: A string containing detailed information about the agent.

### `summary(self)`

The summary method produces a summary of the agent's runtime statistics. It constructs and returns a PrettyTable that includes the start time, end time, and elapsed time of the agent's execution. This summary is valuable for evaluating the duration and performance metrics of the agent's operations.

- **Returns**:
  - `str`: A summary of the agent's run, including start time, end time, and elapsed time.

### `setStartState(self, nodeId)`

The setStartState method allows the agent's starting position to be explicitly set to a specified node identified by nodeId. It updates the agent's current node to the node with the provided ID within the graph. If successful, it changes the visual representation of the agent in the graph world to reflect its new starting position. If the specified node ID is invalid (not present in the graph), a ValueError is raised to indicate the problem.

- **Parameters**:
  - `nodeId` (`str`): The ID of the node to set as the start state.

- **Raises**:
  - `ValueError`: If the specified node ID is invalid.

### `setAlgorithmCallBack(self, algorithmCallBack)`

This method sets the callback function that the agent will execute when runAlgorithm is called. The algorithmCallBack parameter should be a function that defines the algorithm or action sequence the agent will perform. Once set, this callback function dictates the behavior of the agent during algorithm execution.

- **Parameters**:
  - `algorithmCallBack` (`function`): The callback function to be set.

- **Returns**:
  - `None`

### `runAlgorithm(self)`

The runAlgorithm method initiates the execution of the algorithm specified by the callback function set through setAlgorithmCallBack. It begins by marking the root node of the graph with an initial heat map value and records the start time of the algorithm's execution. If no callback function has been set (i.e., algorithmCallBack is None), the method raises a ValueError to indicate that the algorithm cannot proceed without a defined action plan.

- **Raises**:
  - `ValueError`: If the algorithm callback function is not set.

### `getHeatMapColor(self, value: float)`

The getHeatMapColor method determines and returns the color representation corresponding to a given numeric value on a heat map. It employs an exponential decay function to map the provided value to a color gradient, enhancing visualization of the agent's path or activity intensity within the graph world.

- **Parameters**:
  - `value` (`float`): The value to map to a color on the heat map.

- **Returns**:
  - `tuple`: The RGB color value for the given value on the heat map.

### `checkGoalState(self, node)`

This method checks whether a given node within the graph represents a goal state for the agent. It takes a GraphNode object as its parameter and evaluates whether the node's isGoalState attribute is True. If the node is identified as a goal state, the method returns True; otherwise, it returns False. This check allows the agent to assess its progress towards predefined objectives within the graph.

- **Parameters**:
  - `node` (`GraphNode`): The node to be checked.

- **Returns**:
  - `bool`: True if the node is a goal state, False otherwise.

### `moveAgent(self, node, delay:int=1)`

The moveAgent method directs the agent to navigate from its current node to a specified node within the graph. It includes an optional delay parameter that introduces a pause (in seconds) before the agent proceeds to the next node. During the movement process, the method updates the heat map visualization to reflect the agent's path and increments the heat map value of the current node. If successful, the method returns True; otherwise, it returns False if the specified node is None, indicating a failed attempt to move.

- **Parameters**:
  - `node` (`GraphNode`): The node to which the agent should be moved.
  - `delay` (`int`, optional): The delay (in seconds) before moving to the next node. Defaults to 1 second.

- **Returns**:
  - `bool`: True if the agent was successfully moved to the node, False otherwise.

