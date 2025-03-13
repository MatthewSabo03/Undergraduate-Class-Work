nodes = ['AA', 'AC', 'AD', 'AF', 'AG', 'AJ', 
         'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
         'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CJ',
         'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ',
         'EA', 'ED', 'EE', 'EF', 'EG', 'EH', 'EJ']
graph = {
    'AA': {'AC','CA'},'AC': {'BC','AA'},'AD': {'AF','BD'},'AF': {'BF','AD'},'AG': {'AJ','BG'},'AJ': {'BJ','AG'},
    'BB': {'BC'},'BC': {'BB','AC'},'BD': {'AD','BE'},'BE': {'BD','CE'},'BF': {'BG','AF'},'BG': {'AG','CG','BF'},'BH': {'CH'},'BI': {'DI','BJ'},'BJ': {'BI','AJ'},
    'CA': {'CB','AA'},'CB': {'DB','CA'},'CC': {'CD','DC'},'CD': {'CC'},'CE': {'BE','CF','DE'},'CF': {'DF','CE'},'CG': {'CH','BG'},'CH': {'BH','CG'},'CJ': {'DJ'},
    'DA': {'DB','EA'},'DB': {'CB','DA','DC'},'DC': {'DB','CC'},'DD': {'ED','DE'},'DE': {'DD','CE','EE'},'DF': {'CF','DG'},'DG': {'DF'},'DH': {'DI','EH'},'DI': {'BI','DH','DJ'},'DJ': {'DI','CJ'},
    'EA': {'DA','ED'},'ED': {'EA','DD'},'EE': {'DE','EF'},'EF': {'EE'},'EG': {'EH'},'EH': {'DH','EG','EJ'},'EJ': {'EH'}
    }

node_coords= {
    'AA': (1,1),'AC': (3,1),'AD': (4,1),'AF': (6,1),'AG': (7,1),'AJ': (10,1),
    'BB': (2,2),'BC': (3,2),'BD': (4,2),'BE': (5,2),'BF': (6,2),'BG': (7,2),'BH': (8,2),'BI': (9,2),'BJ': (10,2),
    'CA': (1,3),'CB': (2,3),'CC': (3,3),'CD': (4,3),'CE': (5,3),'CF': (6,3),'CG': (7,3),'CH': (8,3),'CJ': (10,3),
    'DA': (1,4),'DB': (2,4),'DC': (3,4),'DD': (4,4),'DE': (5,4),'DF': (6,4),'DG': (7,4),'DH': (8,4),'DI': (9,4),'DJ': (10,4),
    'EA': (1,5),'ED': (4,5),'EE': (5,5),'EF': (6,5),'EG': (7,5),'EH': (8,5),'EJ': (10,5)
    }


def searchDijsktra(graph, start, end, robust_output):
    # List of all nodes, will remove current node after bring visited
    unvisited_nodes = [nodes]
    # Added to after visiting a node
    visited_nodes = []
    # Dictionary to keep track of distances between 2 nodes
    distance = {node: float('inf') for node in graph}
    # Dictionary to keep track of the shortest path between start and end
    shortest_path = {}
    distance[start] = 0
    curr_node = start
    return distance

#print(searchDijsktra(graph,'AA','BB',robust_output=False))

curr_node = 'AA'
#for adj in graph[curr_node]:
    # calculate the distance between the curr_node and the adjacency and then updates distance dictionary
    
adj_coords = node_coords[adj]
            coord_diff = (abs(curr_coords[0]-adj_coords[0]), abs(curr_coords[1]-adj_coords[1]))
            if coord_diff[0] == 0:
                # Adds Y value as adj distance 
                distance[adj] = coord_diff[1]
            else:
                # Adds X value as adj distance
                distance[adj] = coord_diff[0]
            if (min_dist_adj == None or distance[adj]<min_distance) and adj in unvisited_nodes:
                min_distance = distance[adj]
                min_dist_adj = adj