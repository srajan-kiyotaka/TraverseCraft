class CreateWorld:
    def __init__(self, worldName, n, m):
        self.worldName = worldName
        self.n= n
        self.m = m
        self.world = [[0] * n for _ in range(m)]

    def printWorld(self):
        print(self.worldName)
        print(self.world)
    def blockPath(self, arr):
        for i in range(len(arr)):
            x = arr[i][0]
            y = arr[i][1]
            self.world[x][y] = 1

world = CreateWorld("Grid",10,5)
world.blockPath([[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]])
world.printWorld()