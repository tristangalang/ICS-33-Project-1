import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    nodes_dict = defaultdict(set)
    for line in file:
        nodes_dict[line[0]].add(line[2])
        
    return dict(nodes_dict)

def graph_as_str(graph : {str:{str}}) -> str:
    string_format = ''
    for key,value in sorted( graph.items(), key = (lambda x : x[0]) ):
        string_format += f'  {key} -> {sorted(list(value))}\n'
    return string_format
        
        
      
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:    
    reached_set = set()
    exploring_list = [start]
    trace_string = ''
    while len(exploring_list) != 0:
        removed_value = exploring_list.pop(0)
        reached_set.add(removed_value)
        trace_string += f'reached set = {reached_set} \nexploring_list = {exploring_list}\nmoving node {removed_value} from the exploring list into the reached set \nafter adding all nodes reachable directly from a but not already in reached, exploring = {exploring_list} \n\n'
        if removed_value in graph.keys():
            for value in graph[removed_value]:
                if not value in reached_set:
                    exploring_list.append(value)
        if trace:
            print(trace_string)
       
    return reached_set
    
if __name__ == '__main__':
    # Write script here
    graph = read_graph(open(input('Specify the file name representing the graph: ')))
    print(graph_as_str(graph))
    starting_node = input('Specify one start node (or terminate): ')
    if not starting_node in graph:
        print(f"\tEntry error: '{starting_node}'; Illegal: not a source node\n\tPlease enter a legal string")
        starting_node = input('Specify one start node (or terminate): ')
    while starting_node != 'terminate':
        trace_choice = input('Specify choice for tracing algorithm[True]: ')
        if trace_choice == 'False':
            reachable_nodes = reachable(graph, starting_node)
            print(f'From the start node {starting_node}, reachable nodes = {reachable_nodes}')
        elif trace_choice == 'True':
            reachable_nodes = reachable(graph, starting_node, True)
        starting_node = input('\nSpecify one start node (or terminate): ')
    # For running batch self-tests
    """print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()"""
