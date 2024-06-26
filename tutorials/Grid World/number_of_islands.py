from traverseCraft.world import CreateGridWorld
from traverseCraft.agent import GridAgent

def solver(grid, n:int, m:int, i:int, j:int, agent:GridAgent)->int:
    # Base Case
    grid[i][j] = -1
    # move top
    if(i > 0 and grid[i-1][j] == 1 and agent.moveAgent(i - 1, j, delay=0.28)):
        solver(grid, n, m, i - 1, j, agent)
        agent.moveAgent(i, j)
    # move down
    if(i < (n - 1) and grid[i+1][j] == 1 and agent.moveAgent(i + 1, j, delay=0.28)):
        solver(grid, n, m, i + 1, j, agent)
        agent.moveAgent(i, j)
    # move right
    if(j < (m - 1) and grid[i][j+1] == 1 and agent.moveAgent(i, j + 1, delay=0.28)):
        solver(grid, n, m, i, j + 1, agent)
        agent.moveAgent(i, j)
    # move left
    if(j > 0 and grid[i][j-1] == 1 and agent.moveAgent(i, j - 1, delay=0.28)):
        solver(grid, n, m, i, j - 1, agent)
        agent.moveAgent(i, j)

def numIslands(grid, n:int, m:int, agent:GridAgent)->int:
    ans = 0
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == 1):
                ans += 1
                if((i + j) != 0):
                    agent.moveAgent(i, j)
                solver(grid, n, m, i, j, agent)
    return ans

if __name__ == "__main__":
    n = 5
    m = 7
    grid = [[1, 1, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1]]
    water = []
    land = []
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == 0):
                water.append([i, j])
            else:
                land.append([i, j])

    world = CreateGridWorld(worldName = "Number of Islands", rows = n, cols = m, cellSize = 36)
    world.constructWorld()
    world.setBlockPath(water)
    world.setGoalState(land)
    agent = GridAgent(world, agentName = "Robot")
    def sim():
        print("Starting the simulation!")
        print("Number of unique Islands: ", numIslands(grid, n, m, agent))
        print("Simulation Completed!")
    world.setAgent(agent)
    agent.setAlgorithmCallBack(sim)
    world.showWorld()
