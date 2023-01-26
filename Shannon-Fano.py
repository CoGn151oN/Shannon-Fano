
readit = "hello world"


def make_list(scanner) -> list:
    """
    Parameters
    ----------
    scanner: str
        Takes string of text from user input to be analyzed for encryption.

    Returns
    -------
    list
        2d array [letter, probability] sorted descending by 2nd element.
    """
    char_map = {}
    prob = []
    scan_len = len(scanner)

    # create dict with embedded d{count, probability}
    for char in scanner:
        if char not in char_map:
            char_map[char] = {"count": 1, "probability": 0}
        else:
            char_map[char]["count"] += 1
        char_map[char]["probability"] = round(char_map[char]["count"] / scan_len, 2)

    # sort dict to [char, prob]
    for ch, d in char_map.items():
        prob.append([ch, d['probability']])

    # sort by prob
    prob_sort = sorted(prob, key=lambda x: x[1], reverse=True)

    return prob_sort



"""
is len of set(readit) = 0?
    -yes, break
    -no
        split in 2 based on probability total
        assign 0          assign 1
        put in code       put in code
        
        recursion till done
        
        **put in ascending order by pi and keep pop-ing next till sum >= to mid of total pi for current working set
    
        **take 2 new forks and assign 0 and 1
        **if len of fork = 1 then pass
            else recursion
"""








# probs = make_list(readit)
# a = set(readit)
# l = len(a)
#
# take = probs.pop(0)
# print(take)
# print(probs)
# s = 0
# for arr in probs:
#     s += arr[1]
#
# print(s/2)
#
# print("len: ",  l)
# print("\n\n unique set of chars:\n", a)
# print("\n\nprobs:\n", probs)




"""
length of code for sh-fa-alg
b = math.ceil(math.log((1/a), 2))
"""











