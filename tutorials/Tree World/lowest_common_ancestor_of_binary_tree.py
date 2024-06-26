from traverseCraft.world import CreateTreeWorld
from traverseCraft.agent import TreeAgent

def lowestCommonAncestor(rootId:int, p:int, q:int, agent:TreeAgent, world:CreateTreeWorld)->int:
    if(rootId == None):
        return None
    if(rootId == p or rootId == q):
        return rootId
    children = []
    for child in world.nodeMap[rootId].children:
        agent.moveAgent(child.id, delay=0.5)
        children.append(lowestCommonAncestor(child.id, p, q, agent, world))
        agent.moveAgent(rootId, delay=0.5)

    for child in children:
        if(child == None):
            children.remove(child)
    if(len(children) == 2):
        return rootId
    elif(len(children) == 1):
        return children[0]
    return None
    
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
        'goals': [7, 9]
    }
    world = CreateTreeWorld(worldName = "Lowest Common Ancestor of a Binary Tree", worldInfo = treeInfo, radius = 30)
    world.constructWorld()
    agent = TreeAgent(world, agentName = "Robot")
    world.setAgent(agent)
    def sim():
        print("Starting the simulation!")
        print("Lowest Common Ancestor of 7 and 9: ", lowestCommonAncestor(1, 7, 9, agent, world))
        print("Simulation Completed!")
    agent.setAlgorithmCallBack(sim)
    world.showWorld()