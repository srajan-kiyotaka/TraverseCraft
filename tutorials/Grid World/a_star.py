from traverseCraft.world import CreateGridWorld
from traverseCraft.agent import GridAgent

gridWorld = CreateGridWorld(worldName="Simple Grid World", cols=7, rows=7, cellSize=36)
gridWorld.constructWorld()

gridWorld.setBlockPath(blockCells=[[1,1],[2,2],[3,3],[4,3]])

gridAgent = GridAgent(agentName="Simple Grid Agent", world=gridWorld, agentPos=[0,0])
gridWorld.setAgent(agent=gridAgent)

def heuristic(pos, goal):
    # Manhattan distance heuristic
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def astar(agent, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        open_list.sort()
        current = open_list.pop(0)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = current[0] + di, current[1] + dj
            if 0 <= ni < 7 and 0 <= nj < 7 and not agent.checkBlockState(ni, nj):
                tentative_g_score = g_score[current] + 1
                if (ni, nj) not in g_score or tentative_g_score < g_score[(ni, nj)]:
                    came_from[(ni, nj)] = current
                    g_score[(ni, nj)] = tentative_g_score
                    f_score = tentative_g_score + heuristic((ni, nj), goal)
                    open_list.append((f_score, (ni, nj)))

    return None

def toDo():
    start = (0, 0)
    goal = (6, 6)

    path = astar(gridAgent, start, goal)

    if path:
        print("Found path:", path)
        for pos in path[1:]:
            gridAgent.moveAgent(pos[0], pos[1])
            print("Agent moved to:", pos)
        print("Agent reached the goal state!")
    else:
        print("No path found. Agent could not reach the goal state!")

gridAgent.setAlgorithmCallBack(toDo)
gridWorld.showWorld()

print(gridWorld.summary())
print(gridAgent.summary())
