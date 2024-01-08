from world import CreateGridWorld
from tkinter import Frame, Tk
import time
class Agent(CreateGridWorld):
    def __init__(self, worldName, rows, cols, cellSize=10, pathColor="gray", blockColor="red", goalColor="green", cellPadding=2, borderWidth=1, treeCellColor="brown",agentPos=[0,0]):
        CreateGridWorld.__init__(self, worldName, rows, cols, cellSize, pathColor, blockColor, goalColor, cellPadding, borderWidth)
        self._currentPosition = (agentPos[0],agentPos[1])
    def modifyCellColor(self, i, j, color):
        if 0 <= i < self._rows and 0 <= j < self._cols:
            self._cells[i][j].configure(bg=color)
            self._root.update()
    def moveRight(self):
        i, j = self._currentPosition
        j += 1  # Move to the right
        if 0 <= i < self._rows and 0 <= j < self._cols and self._world[i][j] != -1:
            self.modifyCellColor(*self._currentPosition, self._pathColor)  # Reset the current cell color
            self.modifyCellColor(i, j, "blue")  # Move to the right cell
            self._currentPosition = (i, j)
            return True
        else:
            return False

    def moveLeft(self):
        i, j = self._currentPosition
        j -= 1  # Move to the left
        if 0 <= i < self._rows and 0 <= j < self._cols and self._world[i][j] != -1:
            self.modifyCellColor(*self._currentPosition, self._pathColor)  # Reset the current cell color
            self.modifyCellColor(i, j, "blue")  # Move to the left cell
            self._currentPosition = (i, j)
            return True
        else:
            return False

    def moveUp(self):
        i, j = self._currentPosition
        i -= 1  # Move up
        if 0 <= i < self._rows and 0 <= j < self._cols and self._world[i][j] != -1:
            self.modifyCellColor(*self._currentPosition, self._pathColor)  # Reset the current cell color
            self.modifyCellColor(i, j, "blue")  # Move up cell
            self._currentPosition = (i, j)
            return True
        else:
            return False

    def moveDown(self):
        i, j = self._currentPosition
        i += 1  # Move down
        if 0 <= i < self._rows and 0 <= j < self._cols and self._world[i][j] != -1:
            self.modifyCellColor(*self._currentPosition, self._pathColor)  # Reset the current cell color
            self.modifyCellColor(i, j, "blue")  # Move down cell
            self._currentPosition = (i, j)
            return True
        else:
            return False

    def animateMove(self, move_function, steps=10, delay=0.2):
        for _ in range(steps):
            if move_function():
                self.updateWorld()  # Update the world after each move
                self._root.update()
                time.sleep(delay)
            else:
                break

agent_world = Agent("Agent Test Run", rows=30, cols=30, cellSize=20,agentPos=[2,2])
agent_world.constructWorld()
agent_world.addBlockPath([[0, 0], [1, 1], [4, 2], [7, 3], [8, 4], [2, 5], [9, 6], [2, 7]])
agent_world.modifyCellColor(*agent_world._currentPosition, "blue")
agent_world.animateMove(agent_world.moveRight, steps=12)
agent_world.animateMove(agent_world.moveDown, steps=12)
agent_world.animateMove(agent_world.moveUp, steps=12)
agent_world.animateMove(agent_world.moveLeft, steps=12)
agent_world.showWorld()

