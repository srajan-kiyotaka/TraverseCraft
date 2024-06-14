# Tree World

Class representing a tree world.

## Parameters

- **worldName (str)**: The name of the world.
- **worldInfo (dict)**: A dictionary containing information about the world.
  - 'root' (str): The ID of the root node.
  - 'goals' (list): List of goal node IDs.
  - 'adj' (dict): Adjacency list representing tree connections.
  - 'position' (dict): Dictionary of node positions with node IDs as keys.
  - 'edges' (dict, optional): Dictionary of edge information. Default is None.
  - 'vals' (dict, optional): Dictionary of node values. Default is None.
- **radius (int)**: The radius of the nodes in the world visualization. Default is 20.
- **fontSize (int)**: The font size of the node labels. Default is 12.
- **fontBold (bool)**: Whether to use bold font for the node labels. Default is True.
- **fontItalic (bool)**: Whether to use italic font for the node labels. Default is True.
- **nodeColor (str)**: The color of the nodes. Default is "gray".
- **rootColor (str)**: The color of the root node. Default is "red".
- **goalColor (str)**: The color of the goal nodes. Default is "green".
- **width (int)**: The width of the world visualization canvas. Default is SCREEN_WIDTH.
- **height (int)**: The height of the world visualization canvas. Default is SCREEN_HEIGHT.
- **lineThickness (int)**: The thickness of the lines connecting the nodes. Default is 2.
- **arrowShape (tuple)**: The shape of the arrows indicating the direction of the edges. Default is (10, 12, 5).
- **buttonBgColor (str)**: The background color of the buttons. Default is "#7FC7D9".
- **buttonFgColor (str)**: The foreground color of the buttons. Default is "#332941".
- **textFont (str)**: The font family of the button text. Default is "Helvetica".
- **textSize (int)**: The font size of the button text. Default is 24.
- **textWeight (str)**: The font weight of the button text. Default is "bold".
- **buttonText (str)**: The text displayed on the buttons. Default is "Start Agent".
- **logoPath (str, optional)**: The file path to the logo image. Default is "design 1.png".

## Attributes

- **worldID (str)**: Class identifier for the tree world.
- **nodeMap (dict)**: Dictionary mapping node IDs to canvas objects.
- **root**: The root of the tree data structure.
- **_agent**: The agent in the world.

## Methods

### `__init__(self, worldName, worldInfo, radius=20, fontSize=12, fontBold=True, fontItalic=True, nodeColor="gray", rootColor="red", goalColor="green", width=SCREEN_WIDTH, height=SCREEN_HEIGHT, lineThickness=2, arrowShape=(10, 12, 5), buttonBgColor="#7FC7D9", buttonFgColor="#332941", textFont="Helvetica", textSize=24, textWeight="bold", buttonText="Start Agent", logoPath=None)`

The initializer method sets up the attributes of the CreateTreeWorld class. It takes parameters such as worldName (the name of the world), worldInfo (a dictionary containing essential information about the world like root node, goal nodes, adjacency list, and node positions), and various visual and UI parameters for rendering the world. It initializes the canvas, constructs the tree data structure, and prepares the GUI elements like buttons and node representations.

### `aboutWorld()`

This method generates a textual description of the attributes of the world. It creates a formatted table using PrettyTable library, listing details such as the world name, root node ID, goal nodes, visualization parameters (radius, colors, font settings), and UI configurations (button colors, text attributes).

### `summary()`

The summary() method provides a concise overview of the world by displaying the number of visits to each node. It uses PrettyTable to create a table listing each node ID along with its corresponding visit count.

### `constructWorld()`
 
This method constructs the visual representation of the tree world. It calls private methods _drawEdges(), _drawNodes(), and _addStartButton() to render edges, nodes, and UI controls on the canvas.


### `changeNodeColor(nodeId, color)`

Allows changing the color of a specific node identified by nodeId on the canvas to the specified color. This method updates the visual representation of the node in the tree world.

- **nodeId (int)**: The ID of the node to change the color of.
- **color (str)**: The new color to set for the node.

### `changeNodeText(nodeId, newText)`

Enables updating the text label of a specific node identified by nodeId on the canvas to the provided newText. This method modifies the displayed text associated with the node.

- **nodeId (int)**: The ID of the node to change the text of.
- **newText (str)**: The new text to set for the node.

### `getNode(nodeId)`

Returns the pointer to the node object with the given nodeId. This method facilitates access to specific nodes within the tree data structure based on their unique identifiers.

- **nodeId**: The ID of the node to retrieve the pointer for.

### `setAgent(agent)`

Sets the agent (if applicable) that will interact with the tree world. The agent can be a separate class responsible for algorithmic operations or simulations within the world.

- **agent (Agent)**: The agent to be set.

### `showWorld()`

Starts the graphical user interface (GUI) main loop, displaying the constructed tree world and allowing user interaction through the Tkinter window.

### `__str__()`

Provides a string representation of the CreateTreeWorld instance, summarizing its attributes and configurations. It calls aboutWorld() internally to generate this textual description.
