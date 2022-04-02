import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    nodes_dict = defaultdict(set)
    lines_list = list(open(file))
    for line in lines_list:
        nodes_dict[line[0]].add(line[2])
        
    return dict(nodes_dict)

def graph_as_str(graph : {str:{str}}) -> str:
    string_format = ''
    for key,value in sorted( graph.items(), key = (lambda x : x[0]) ):
        string_format += f'  {key} -> {list(value)}\n'
    return string_format
        
        
      
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    pass





if __name__ == '__main__':
    # Write script here
    """main_dict = read_graph('graph1.txt')
    print(main_dict['c'])
    print(main_dict)"""
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
