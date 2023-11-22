dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
res = dict((i, dct[i]) for i in dct if dct[i] > 2)

# for i in dct:
#     if dct[i] > 2:
#         res[i] = dct[i]

print(res)
