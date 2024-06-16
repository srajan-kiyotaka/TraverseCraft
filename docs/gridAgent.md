# GridAgent Class

The `GridAgent` class represents an agent that operates within a grid world environment.

## Initialization

### `__init__(self, world, agentName:str, agentColor:str="blue", heatMapView:bool=True, heatMapColor:str="#FFA732", agentPos:tuple=(0,0), heatGradient:float=0.05):`

The constructor initializes an instance of the `GridAgent` class, which represents an agent operating within a grid-based world.

- **Parameters**:

- `world` (CreateGridWorld): The grid world object in which the agent operates.
- `agentName` (str): The name of the agent.
- `agentColor` (str, optional): The color of the agent. Defaults to "blue".
- `heatMapView` (bool, optional): Whether to enable the heat map view. Defaults to True.
- `heatMapColor` (str, optional): The color of the heat map. Defaults to "#FFA732".
- `agentPos` (tuple, optional): The initial position of the agent. Defaults to (0, 0).
- `heatGradient` (float, optional): The gradient value for the heat map. Defaults to 0.05.

## Attributes

- `algorithmCallBack` (function): Callback function for the agent's algorithm.

## Public Methods

### `__str__()`

Returns a string describing the attributes of the agent.

### `aboutAgent()`

Prints information about the agent including its name, color, and the world it operates in.

### `summary()`

Returns a summary of the agent's run including start time, end time, and elapsed time.

### `setStartState(i: int, j: int)`

Sets the start state of the agent to the specified position (i, j) on the grid world.

- Raises `ValueError` if the specified start position is invalid.

### `setAlgorithmCallBack(algorithmCallBack: function)`

Sets the callback function for the agent's algorithm.

### `runAlgorithm()`

Executes the callback function set by `setAlgorithmCallBack()`. Raises `ValueError` if the callback function is not set.

### `getHeatMapColor(value: float)`

Maps a numeric value to a color on the heat map.

- Args:
  - `value` (float): The value to be mapped.

- Returns:
  - `str`: The RGB color string representing the mapped value on the heat map.

### `moveAgent(i: int, j: int, delay: float=0.5)`

Moves the agent to the specified position (i, j) on the grid world.

- Args:
  - `i` (int): The row index of the target position.
  - `j` (int): The column index of the target position.
  - `delay` (float, optional): The delay in seconds before moving the agent. Defaults to 0.5 seconds.

- Returns:
  - `bool`: True if the agent successfully moves to the target position, False otherwise.

### Internal Methods

These methods are not intended to be directly called by users but support the functionality of the class:

- `_warmerColor(color: str, sValue: float)`: Generates a warmer color from the given color based on saturation value.
- `checkGoalState(i: int, j: int)`: Checks if the specified position (i, j) on the grid world is a goal state.
- `checkBlockState(i: int, j: int)`: Checks if the specified position (i, j) on the grid world is blocked or empty.


## Usage

The `GridAgent` class provides methods to control the agent's movement within a grid world, interact with its environment, and visualize heat maps. It serves as a foundation for implementing agent-based simulations and experiments within defined grid-based environments.
