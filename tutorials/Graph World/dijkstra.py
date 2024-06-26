from traverseCraft.world import CreateGraphWorld
from traverseCraft.agent import GraphAgent
import heapq
from prettytable import PrettyTable

def dijkstra(startNode, world, agent):
    # Initialize distances with infinity and set start node distance to 0
    distances = {node: float('inf') for node in world.nodeMap.keys()}
    previous_nodes = {node: None for node in world.nodeMap.keys()}
    distances[startNode] = 0
    priority_queue = [(0, startNode)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # If the current distance is greater than the recorded distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        agent.moveAgent(current_node, delay=0.3)
        
        curr_node = world.nodeMap[current_node]

        for neighbor, weight in zip(curr_node.neighbors, curr_node.edges):
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor.id]:
                distances[neighbor.id] = distance
                previous_nodes[neighbor.id] = current_node
                heapq.heappush(priority_queue, (distance, neighbor.id))
                
    return distances, previous_nodes

def get_path(previous_nodes, startNode, targetNode):
    path = []
    current_node = targetNode
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path if path[0] == startNode else []

if __name__ == "__main__":
    graphInfo = {
        'adj': {
            'A': ['B', 'C', 'D'],
            'B': ['D', 'E'],
            'C': ['D', 'F'],
            'D': ['A', 'E', 'F'],
            'E': ['D', 'I'],
            'F': ['J', 'K'],
            'G': ['I'],
            'H': ['G', 'L'],
            'I': ['E', 'H', 'J'],
            'J': ['H', 'I', 'L'],
            'K': ['L', 'M'],
            'L': ['M'],
            'M': []
        },
        'position': {
            'A': (100, 300),
            'B': (200, 200),
            'C': (200, 400),
            'D': (300, 300),
            'E': (400, 200),
            'F': (400, 400),
            'G': (600, 100),
            'H': (700, 200),
            'I': (500, 200),
            'J': (500, 300),
            'K': (600, 400),
            'L': (700, 300),
            'M': (700, 400)
        },
        'edges': {
            'A': [3, 4, 5],
            'B': [1, 4],
            'C': [5, 1],
            'D': [5, 2, 2],
            'E': [1, 1],
            'F': [1, 2],
            'G': [1],
            'H': [1, 2],
            'I': [2, 1, 2],
            'J': [1, 2, 4],
            'K': [3, 8],
            'L': [4],
            'M': []
        },
        'goals': ['M']
    }
    world = CreateGraphWorld(worldName="Dijkstra's Algorithm", worldInfo=graphInfo, radius=30)
    world.constructWorld()
    agent = GraphAgent(world, agentName="TraversalAgent", heatMapView=False)
    agent.setStartState('A')
    world.setAgent(agent)
    def sim():
        print("Starting the simulation!")
        distances, previous_nodes = dijkstra('A', world, agent)
        
        # Create a table to display shortest distances and paths
        table = PrettyTable(['Node', 'Shortest Distance from A', 'Path'])
        for node in world.nodeMap.keys():
            path = get_path(previous_nodes, 'A', node)
            table.add_row([node, distances[node], " -> ".join(path)])
        print(table)
        print("Simulation Completed!")
    agent.setAlgorithmCallBack(sim)
    world.showWorld()
