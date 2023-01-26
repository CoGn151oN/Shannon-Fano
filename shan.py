import numpy as np
import pandas as pd


def listify(scanner) -> list:
    """
    Parameters
    ----------
    scanner: str
        Takes string arg from user input.

    Returns
    -------
    list
        2d array of:
            - unique values
            - their counts
            - probabilites (frequency of occurrence)
            - expected length of Shannon code
        sorted by counts in descending order.
    """
    ct = []
    cum_pi = []

    # unique chars
    uniq = np.unique(np.array([x for x in scanner]))

    # counts
    for char in uniq:
        ct.append(scanner.count(char))
    count = np.array(ct)

    # sets permutation sorting based on counts in descending order
    perm = count.argsort()[::-1]

    # probabilities
    pi = np.round(count/len(scanner), 5)

    # cumulative probabilities taken from sorted pi arr
    for i in range(len(pi)):
        cum_pi.append(sum(pi[perm][0:i]))

    sum_pi = np.array(cum_pi)

    # expected length based on log2(1/pi)
    exp_len = np.ceil(np.log2((1/pi)))

    # binary code arr with len of exp_len from sum_pi
    shan_code = []
    for e, x in enumerate(sum_pi):
        n = x
        txt = "0."
        while len(txt) < exp_len[perm][e] + 2:
            n *= 2
            if n > 1:
                txt += "1"
                n -= 1
            else:
                txt += "0"
        shan_code.append(txt)

    return [uniq[perm], count[perm], pi[perm], exp_len[perm], sum_pi, shan_code]


if __name__ == '__main__':
    read_it = input("type..")
    df = pd.DataFrame(data=listify(read_it), index=["Char", "Count", "Pi", "Len", "CumlPi", "Code"])
    print(df)
