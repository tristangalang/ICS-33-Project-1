import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    match_pref = dict()
    for lines in open_file:
        line_split = lines.rstrip('\n').split(';')
        person = line_split[0]
        preferences = line_split[1:]
        preferences_list = [None, preferences]
        match_pref[person] = preferences_list
    return match_pref
        


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    pref_str = ''
    for person in sorted(d.keys(), key = key, reverse = reverse):
        pref_str += f'  {person} -> {d[person]}\n'
    return pref_str
        


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    index = order.index(p1)
    index2 = order.index(p2)
    true_index = index
    if index2 < index:
        true_index = index2
        
    return order[true_index]


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    # match_set = set()
    # for man in men:
    #     match_tuple = (man, men[man][0])
    #     match_set.add(match_tuple)
    # return match_set
    return {(man, men[man][0]) for man in men}

def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_copy = men.copy()
    dicto = men_copy
    unmatched = {men for men in dicto.keys()}
    #match_set = set()
    while len(unmatched) != 0:
        man = unmatched.pop()
        removed_woman = dicto[man][1].pop(0)
        if women[removed_woman][0] == None: #if woman is unmatched, automatically match her with the man
            dicto[man][0] = removed_woman
            #matched = (man, removed_woman)
            women[removed_woman][0] = man
            #match_set.add(matched)
            #women[removed_woman][0] = man
        elif women[removed_woman][0] != None: #if current woman has a match already
            preference = who_prefer(women[removed_woman][1], man, women[removed_woman][0])
            if preference == man: ### updates the the previous man with the actual preference             
                #matched = (preference, removed_woman)
                #match_set.add(matched)
                unmatched.add(women[removed_woman][0])
                dicto[women[removed_woman][0]][0] = None
                dicto[man][0] = removed_woman
                women[removed_woman][0] = preference #replaces the previous match, with the actual preference
                #dicto[women[removed_woman][0]][0] = None #once rejected, man's initial match is left and turns to none
                a = dicto[women[removed_woman][0]][0]
            else:
                unmatched.add(man)
                # index = dicto[man][1].index(removed_woman)
                # print(index)
                #dicto[man][1].pop(index)
    matches = extract_matches(dicto)
    return matches
            
            
            
        # for woman in women.keys():
        #     if woman == removed_woman and women[woman][0] == None:
        #         matched = (man, removed_woman)
        #         match_set.add(matched)
        #     elif woman == removed_woman and women[woman][0] != None:
        #         preference = who_prefer(women[woman][1], man, women[woman][0])
        #         if preference == man: ### updates the the previous man with the actual preference 
        #             matched = (preference, removed_woman)
        #             match_set.add(matched)
        #             unmatched.add(women[woman][0])
        #             women[woman][0] = preference #replaces the none
        #         else:
        #             unmatched.add(man)
                    
    
    
if __name__ == '__main__':
    # Write script here
    # men_txt = goody.safe_open('Specify file name - men: ', 'r', 'improper file')
    # women_txt = goody.safe_open('Specify file name - women: ', 'r', 'improper file')
    # men_dict = read_match_preferences(men_txt)
    # women_dict = read_match_preferences(women_txt)
    # print(dict_as_str(men_dict))
    # print('\n',dict_as_str(women_dict))
    # trace = input('Specify choice for tracing algorithm[True] ')
    # if trace == 'False':
    #     make_match(men_dict, women_dict, False)
    # elif trace == 'True':
    #     print('Unfinished')
    #     pass
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
