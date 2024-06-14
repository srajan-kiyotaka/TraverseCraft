# Data Structures Module

The Data Structures module provides fundamental classes for constructing and manipulating tree and graph structures used within the World module.

## TreeNode Class

The `TreeNode` class represents a node in a tree structure. It encapsulates the following attributes:

- `id` (int or str): Unique identifier for the node.
- `val` (any, optional): Value associated with the node. Defaults to `label` if not provided.
- `children` (list of TreeNode objects): List of child nodes.
- `edges` (list of int or float, optional): List of edge weights corresponding to each child node. Defaults to a list of 1s if not provided and children are present.
- `isGoalState` (bool): Indicates if the node is a goal state.
- `_heatMapValue` (int): Internal attribute used for heat map visualization (default is 0).

### Methods

- `__init__(self, label, children: list, val=None, isGoalState: bool = False, edges: list = [])`: Initializes a TreeNode instance.
- `__str__(self) -> str`: Returns a string representation of the TreeNode object.

The `TreeNode` class is used extensively in the World module to build hierarchical tree structures. Users can instantiate `TreeNode` objects and customize them by inheriting from the class to add additional attributes or methods tailored to specific applications.

## GraphNode Class

The `GraphNode` class represents a node in a graph structure. It encapsulates the following attributes:

- `id` (int or str): Unique identifier for the node.
- `val` (any, optional): Value associated with the node. Defaults to `label` if not provided.
- `neighbors` (list of GraphNode objects): List of neighboring nodes.
- `edges` (list of int or float, optional): List of edge weights corresponding to each neighboring node. Defaults to a list of 1s if not provided and neighbors are present.
- `isGoalState` (bool): Indicates if the node is a goal state.
- `_heatMapValue` (int): Internal attribute used for heat map visualization (default is 0).

### Methods

- `__init__(self, label, neighbors: list, val=None, isGoalState: bool = False, edges: list = [])`: Initializes a GraphNode instance.
- `__str__(self) -> str`: Returns a string representation of the GraphNode object.

The `GraphNode` class is used in the World module to construct complex networked structures. Users can instantiate `GraphNode` objects and extend their functionality by inheriting from the class to introduce additional attributes or methods specific to their needs.

## Customization

These classes provide a solid foundation for creating and manipulating tree and graph structures within the World module. For specialized requirements, users are encouraged to inherit from `TreeNode` and `GraphNode` classes to tailor them according to specific application scenarios.

By leveraging these customizable data structures, developers can effectively manage and visualize complex relationships within their simulated environments.

