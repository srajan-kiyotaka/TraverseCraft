# API Reference for `CreateGridWorld` Class

Class representing the world created using grids.

## Attributes

- `setOfCoordinates`: `List[List[int]]`
- `coordinate`: `List[int]`
- `worldID`: `"GRIDWORLD"`

## Parameters

- `worldName` (`str`): The name of the world.
- `rows` (`int`): The number of rows in the world (between 1 and 1000).
- `cols` (`int`): The number of columns in the world (between 1 and 1000).
- `cellSize` (`int`, optional): Size of each cell in pixels (default: 10, between 10 and 50).
- `pathColor` (`str`, optional): Color of path cells (default: "gray").
- `blockColor` (`str`, optional): Color of block cells (default: "red").
- `goalColor` (`str`, optional): Color of goal cells (default: "green").
- `cellPadding` (`int`, optional): Padding around each cell in pixels (default: 2).
- `borderWidth` (`int`, optional): Width of cell borders in pixels (default: 1).
- `buttonBgColor` (`str`, optional): Background color of the button (default: "#7FC7D9").
- `buttonFgColor` (`str`, optional): Foreground color of the button (default: "#332941").
- `textFont` (`str`, optional): Font of the button text (default: "Helvetica").
- `textSize` (`int`, optional): Size of the button text (default: 24).
- `textWeight` (`str`, optional): Weight of the button text (default: "bold").
- `buttonText` (`str`, optional): Text displayed on the button (default: "Start Agent").
- `logoPath` (`str`, optional): Path to the logo image.

#### Raises

- `ValueError`: If rows or columns are out of valid range.

## Methods

### `aboutWorld(self)`

This method returns a textual description of the world's attributes in a tabular format using the PrettyTable library. It provides details such as the world name, dimensions (rows and columns), cell size, window size, colors for paths, blocks, and goals, as well as button properties like background color, text font, size, and weight.

#### Parameters

- `None`

#### Returns

- `str`: Description of the world attributes.

### `summary(self)`

Generates a summary of the world's grid configuration as a tabular format using PrettyTable. It lists out each cell in the grid along with its corresponding value. This method is useful for debugging and visualizing the initial state of the world.

#### Parameters

- `None`

#### Returns

- `str`: Summary of the world.

### `constructWorld(self)`

This method constructs the graphical user interface (GUI) representation of the world. It initializes the window with the specified dimensions and title, creates cells for each row and column in the grid, sets up event handling for cell toggling (click to block/unblock cells), adds goal cells if provided, and creates a start button for running the agent's algorithm.

#### Parameters

- `None`

#### Returns

- `None`

### `setBlockPath(self, blockCells:setOfCoordinates)`

sets block cells to the world grid, which are cells that cannot be traversed by an agent. It takes a set of coordinates representing the block cells and visually updates the grid to reflect these changes by coloring the corresponding cells in red.

#### Parameters

- `blockCells` (`setOfCoordinates`): Set of coordinates representing block cells.

#### Returns

- `None`

### `setGoalState(self, goalState:setOfCoordinates)`

sets goal cells to the world grid, which represents the target states an agent aims to reach. It takes a set of coordinates representing the goal cells and updates the grid by coloring these cells in green to visually differentiate them from other cells.

#### Parameters

- `goalState` (`setOfCoordinates`): Set of coordinates representing goal cells.

#### Returns

- `None`

### `setAgent(self, agent)`

Sets the agent object that will interact with the world. The agent object passed as an argument should have methods and attributes necessary for running algorithms within the world environment.

#### Parameters

- `agent` (`Agent`): Agent object to set.

#### Returns

- `None`

### `updateWorld(self)`

Updates the graphical representation of the world in the GUI. It iterates over each cell in the grid and ensures they are correctly positioned using the grid layout manager. This method is essential for reflecting any changes made to the world, such as adding or removing blocks/goals.

#### Parameters

- `None`

#### Returns

- `None`

### `showWorld(self)`

Starts the GUI main loop, displaying the constructed world to the user. This method keeps the GUI window open and responsive, allowing interaction with the grid and start button.

#### Parameters

- `None`

#### Returns

- `None`

### Private Methods

Private methods in Python classes are prefixed with an underscore _. These methods are not meant to be accessed directly from outside the class but are utilized internally for implementation details:


- `_setWindowIcon(self, logoPath)`: Sets the window icon using the provided logo path.
- `_toggleCell(self, event, i, j)`: Handles the click event on a cell, toggling its color between path color and block color based on its current state.
- `_startAgent(self)`: Initiates the agent's algorithm execution in a separate thread upon clicking the start button.
- `_disableCellToggle(self)`: Disables the functionality of toggling cell colors, typically called when the agent is running to prevent interference with the algorithm.
