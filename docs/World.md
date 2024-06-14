# World Module API Reference

The `world` module provides functionalities to create and manage different types of worlds using Tkinter-based GUI components.

## Functions

### `getScreenSize() -> tuple`

Returns the screen size for any operating system.

**Raises:**
- `NotImplementedError`: If the operating system is not supported.

**Returns:**
- `tuple`: A tuple containing the width and height of the screen.

## Classes

- [**CreateGridWorld**](./gridWorld.md):
  - Represents a grid-based world environment. This class facilitates the creation, visualization, and manipulation of a grid structure where agents can navigate and interact with nodes.

- [**CreateTreeWorld**](./treeWorld.md):
  - Models a tree-based world environment. It supports operations such as node insertion, deletion, traversal, and visualization within a hierarchical tree structure.

- [**CreateGraphWorld**](./graphWorld.md):
  - Implements a graph-based world environment. This class allows for the creation, visualization, and management of nodes and edges in a graph structure. It supports operations like adding nodes, creating edges, and visualizing connectivity.

---

**Note**: For detailed documentation on each class, click on the respective links above.