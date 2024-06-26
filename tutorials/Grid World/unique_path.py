from traverseCraft.world import CreateGridWorld
from traverseCraft.agent import GridAgent

def solver(n:int, m:int, i:int, j:int, agent:GridAgent)->int:
    # Base Case
    if(i == (n - 1) and j == (m - 1)):
        return 1
    elif((i < 0) or (j < 0) or (i == n) or (j == m)):
        return 0

    ans = 0

    # move right
    if(agent.moveAgent(i, j + 1, delay=0.28)):
        ans += solver(n, m, i, j + 1, agent)
        agent.moveAgent(i, j)

    # move down
    if(agent.moveAgent(i + 1, j, delay=0.28)):
        ans += solver(n, m, i + 1, j, agent)
        agent.moveAgent(i, j)

    return ans

def uniquePaths(m:int, n:int, agent:GridAgent)->int:
    return solver(m, n, 0, 0, agent)

if __name__ == "__main__":
    m = 3
    n = 7
    world = CreateGridWorld(worldName = "Unique Paths", rows = m, cols = n, cellSize = 36)
    world.constructWorld()
    agent = GridAgent(world, agentName = "Robot")
    def sim():
        print("Starting the simulation!")
        print("Number of unique paths: ", uniquePaths(m, n, agent))
        print("Simulation Completed!")
    world.setAgent(agent)
    agent.setAlgorithmCallBack(sim)
    world.showWorld()
