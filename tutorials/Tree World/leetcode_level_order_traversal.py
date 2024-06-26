from traverseCraft.world import CreateTreeWorld
from traverseCraft.agent import TreeAgent
from collections import deque

def levelOrderTraversal(rootId: int, agent: TreeAgent, world: CreateTreeWorld):
    if rootId is None:
        return []
    
    queue = deque([rootId])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node_id = queue.popleft()
            agent.moveAgent(node_id, delay=0.5)
            current_level.append(node_id)

            for child in world.nodeMap[node_id].children:
                queue.append(child.id)
        
        result.append(current_level)
    
    return result

if __name__ == "__main__":
    treeInfo = {
        'adj': {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [],
            5: [8, 9],
            6: [],
            7: [],
            8: [],
            9: []
        },
        'root': 1,
        'position': {
            1: (400, 100),
            2: (200, 200),
            3: (600, 200),
            4: (100, 300),
            5: (300, 300),
            6: (500, 300),
            7: (700, 300),
            8: (200, 400),
            9: (400, 400)
        },
        'goals': []
    }
    world = CreateTreeWorld(worldName="Leetcode Binary Tree Level Order Traversal", worldInfo=treeInfo, radius=30)
    world.constructWorld()
    agent = TreeAgent(world, agentName="TraversalAgent")
    world.setAgent(agent)

    def sim():
        print("Starting the simulation!")
        levels = levelOrderTraversal(1, agent, world)
        print("Level Order Traversal:")
        for level in levels:
            print(level)
        print("Simulation Completed!")

    agent.setAlgorithmCallBack(sim)
    world.showWorld()