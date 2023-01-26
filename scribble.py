# # import math
# import numpy as np
# #
# # a = 0.12
# #
# # b = math.ceil(math.log((1/a), 2))
# # print(b)
#
# s = "hello world"
# uniq = np.unique(np.array([x for x in s]))
# bi = []
# # byte_arr = bytearray(s, "utf8")
# # for b in byte_arr:
# #     bi_e = bin(b)
# #     bi.append(bi_e)
# # print(bi)
#
#
# byte_arr = bytearray(s, "utf8")
# print(byte_arr)


# l = ['l' 'o' 'w' 'r' 'h' 'e' 'd' ' ']
# pi = [0.27, 0.18, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09]
# cum_pi = []
#
# for i in range(len(pi)):
#     cum_pi.append(sum(pi[0:i]))
#
# print(cum_pi)


# add as many different characters as you want

pi = [0.27273, 0.18182, 0.09091, 0.09091, 0.09091, 0.09091, 0.09091, 0.09091]
exp = [2., 3., 4., 4., 4., 4., 4., 4.]
cuml = [0, 0.27273, 0.45455, 0.54546, 0.63637, 0.72728, 0.81819, 0.9091 ]

expl = 5
# n = 0.385
# txt = "0."
cde = []
for e, x in enumerate(cuml):
    n = x
    txt = "0."
    while len(txt) < exp[e]+2:
        n *= 2
        if n > 1:
            txt += "1"
            n -= 1
        else:
            txt += "0"
    cde.append(txt)

print(cde)

"""
for loop iterating over cumulative_pi (exp L??)
    input = n <- take cumulative_pi to start then alter with multiplication
    text = ""

    while len(text) < expected_L (matching current iteration of pi)
        n * 2
        if n>1:
            text += "1"
            n -= 1
        else:
            text += 0

"""


