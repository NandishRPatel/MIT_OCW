from graph import Digraph, Node, WeightedEdge

'''def dp_make_weight(egg_weights, target_weight, memo = {}):
    total_eggs = 0
    for i in egg_weights[::-1]:
        number_of_eggs = target_weight//i
        if number_of_eggs > 0:
            memo[i] = number_of_eggs
            target_weight -= (number_of_eggs*i)
            total_eggs += number_of_eggs

    return total_eggs
'''
def load_map(map_filename):
    file = open(map_filename,'r')
    digraph = Digraph()
    node_list = []
    for line in file.readlines():
        src, dest, total_dist, outdoor_dist = line.split()
        src_node = Node(src)
        dest_node = Node(dest)    
        if not src_node in node_list:digraph.add_node(src_node)
        if not dest_node in node_list:digraph.add_node(dest_node)
        edge = WeightedEdge(src_node, dest_node, int(total_dist), int(outdoor_dist))
        digraph.add_edge(edge)
        node_list.append(src_node)
        node_list.append(dest_node)  
    file.close()
    return digraph


def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,best_path):
    
    if not digraph.has_node(start) and digraph.has_node(end):
        raise ValueError('Node Not Valid')
    path += [start]
    
    if start == end:
        return path
    
    else:
        for edge in digraph.get_edges_for_node(start):
            dist = 0
            outdoor_dist = 0
            child = edge.get_destination()
            if child not in path:
                dist += edge.get_total_distance()
                outdoor_dist += edge.get_outdoor_distance()
                if outdoor_dist <= max_dist_outdoors:
                    if best_path == None or len(path) < len(best_path):
                        newPath = get_best_path(digraph, child, end, path, max_dist_outdoors, best_dist, best_path)
                        if newPath != None:
                            best_path = newPath

            else:print('Already visited', child)
                        
        print(dist,outdoor_dist)
        return path
                

        



if __name__ == "__main__":
    digraph = load_map("mit_map.txt")
    print(get_best_path(digraph,Node("32"),Node("66"),path = [], max_dist_outdoors = 400, best_dist=None, best_path=None))