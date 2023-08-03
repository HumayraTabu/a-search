def a_star_search(start, goal):
        open_fringe = set(start)
        close_fringe = set()
        g = {} 
        parents = {}

        g[start] = 0

        parents[start] = start  

        while len(open_fringe) > 0:
            n = None
            
            for v in open_fringe:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v

            if n == goal or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                   
                    if m not in open_fringe and m not in close_fringe:
                        open_fringe.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight


                   
                    else:
                        if g[m] > g[n] + weight:
                           
                            g[m] = g[n] + weight
                            
                            parents[m] = n

                            if m in close_fringe:
                                close_fringe.remove(m)
                                open_fringe.add(m)

            if n == None:
                print('Path does not exist!')
                return None

            if n == goal:
                path = []
                path_cp = []
                full = {
                'H': "Niketon (Home)",
                'DCC': "Gulshan DCC",
                'MGR': "Mohakhali Gulshan Road",
                'AR': "Airport Road",
                'BIR': "Bir Uttam Road",
                'FG': "Farm gate",
                'GR': "Green Road",
                'PP': "Panta Path",
                'HLR': "Hatirjheel Link Road",
                'KB': "Karwan Bazar",
                'PZ': "Police Plaza",
		        'MR': "Mogbazar Road",
                'U': "UAP"
                }
                while parents[n] != n:
                    path.append(n)
                    path_cp.append(full[n])
                    n = parents[n]

                path.append(start)
                path_cp.append(full[start])
                path.reverse()
                path_cp.reverse()
                print('Path found: {}'.format(str(path_cp).replace(",","-->")))
                return path

            open_fringe.remove(n)
            close_fringe.add(n)

        print('Path does not exist!')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):

        H_dist = {
            'H': 2,
            'DCC': 3,
            'MGR': 1,
            'AR': 5,
            'BIR': 1,
            'FG': 3,
            'GR': 2,
            'MR': 2,
            'KB': 6,
            'PP': 6,
            'HLR': 1,
	        'PZ': 4,
            'U': 0
        }
        return H_dist[n]

Graph_nodes = {
        'H': [('PZ', 2), ('DCC', 3)],
        'DCC': [('PZ', 4),('MGR', 1)],
        'MGR': [('AR', 3)],
        'AR': [('MR', 4),('BIR', 5)],
        'BIR': [('FG', 4)],
        'FG': [('GR', 2)],
        'GR': [('U', 4)],
        'MR': [('KB', 3)],
        'KB': [('GR', 3)],
	    'PZ': [('HLR', 3)],
	    'HLR': [('PP', 5)],
        'PP': [('GR', 4)],
        'U': None
}

path = a_star_search('H', 'U') 

path_cost = 0.0

for i in range(len(path)-1):
    for key, value in Graph_nodes[path[i]]:
        if key == path[i+1]:
            path_cost += value
            break
print("The path cost is %.2f " % path_cost)
