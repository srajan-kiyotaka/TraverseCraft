# API Reference: CreateGraphWorld Class

Class representing a graph world.

## Parameters

- `worldName` (str): The name of the world.
- `worldInfo` (dict): Dictionary containing information about the world.
  - 'goals' (list): List of goal node IDs.
  - 'adj' (dict): Adjacency list representing graph connections.
  - 'position' (dict): Dictionary of node positions with node IDs as keys.
  - 'edges' (dict, optional): Dictionary of edge information. Default is None.
  - 'vals' (dict, optional): Dictionary of node values. Default is None.
- `radius` (int): Radius of nodes in the visualization. Default is 20.
- `fontSize` (int): Font size for node labels. Default is 12.
- `fontBold` (bool): Whether node labels are bold. Default is True.
- `fontItalic` (bool): Whether node labels are italic. Default is True.
- `nodeColor` (str): Color of nodes. Default is "gray".
- `goalColor` (str): Color of goal nodes. Default is "green".
- `width` (int): Width of the visualization canvas. Default is SCREEN_WIDTH.
- `height` (int): Height of the visualization canvas. Default is SCREEN_HEIGHT.
- `lineThickness` (int): Thickness of lines connecting nodes. Default is 2.
- `arrowShape` (tuple): Shape of arrows indicating edge directions. Default is (10, 12, 5).
- `buttonBgColor` (str): Background color of buttons. Default is "#7FC7D9".
- `buttonFgColor` (str): Foreground color of buttons. Default is "#332941".
- `textFont` (str): Font family of button text. Default is "Helvetica".
- `textSize` (int): Font size of button text. Default is 24.
- `textWeight` (str): Font weight of button text. Default is "bold".
- `buttonText` (str): Text displayed on buttons. Default is "Start Agent".
- `logoPath` (str, optional): File path to the logo image. Default is None.

#### Attributes

- `worldID` (str): Class identifier for the graph world.
- `nodeMap` (dict): Dictionary mapping node IDs to canvas objects.
- `root` (TreeNode): The root of the graph data structure.

## Methods

### `aboutWorld()`

Generates and returns a detailed textual representation of the attributes of the graph world. It uses the PrettyTable library to organize and present information such as world name, node colors, button settings, and visualization dimensions in a tabular format.

#### Returns

- `str`: The attributes of the world.

### `summary()`

Creates a summary of the graph world by generating a table that lists each node ID along with its corresponding number of visits. This method is particularly useful for visualizing statistical data related to the exploration of nodes within the graph.

#### Returns

- `str`: The summary of the world.

### `constructWorld()`

Initiates the process of constructing the graphical representation of the graph world. It calls internal methods _drawEdges, _drawNodes, and _addStartButton to draw edges between nodes, visualize nodes themselves, and add a start button for agent interaction.

### `changeNodeColor(nodeId: int, color: str)`

Changes the color of a specific node identified by nodeId to the new color specified by color. This method updates the visual representation on the canvas by modifying the fill color of the corresponding node object.

#### Parameters

- `nodeId` (int): ID of the node to change the color of.
- `color` (str): New color to set for the node.

### `changeNodeText(nodeId: int, newText: str)`

Updates the text displayed on a node identified by nodeId to newText. This method modifies the text attribute of the node label object associated with the specified node on the visualization canvas.

#### Parameters

- `nodeId` (int): ID of the node to change the text of.
- `newText` (str): New text to set for the node.

### `getNode(nodeId: int)`

Retrieves and returns the node object corresponding to the provided nodeId. This method is useful for accessing specific nodes within the graph world, allowing external components or agents to interact with individual nodes directly.

#### Parameters

- `nodeId` (int): ID of the node to retrieve the pointer for.

#### Returns

- `Node`: Pointer to the node with the given `nodeId`.

### `setAgent(agent: Agent)`

Sets the agent that will interact with the graph world. The agent parameter should be an instance of an agent class capable of running algorithms within the context of the graph world. This method prepares the environment for agent-based simulations or algorithms.

#### Parameters

- `agent` (Agent): The agent to be set.

### `showWorld()`

Displays the constructed graph world visualization to the user. This method starts the main event loop of the Tkinter application, allowing the graphical user interface (GUI) to render and remain interactive until the user closes the window or exits the application.

### `__str__()`

This method returns a string that describes the attributes of the graph world. It utilizes the aboutWorld() method to generate a human-readable summary of the key attributes such as world name, dimensions, node colors, and button settings.

#### Returns

- `str`: The attributes of the world.
