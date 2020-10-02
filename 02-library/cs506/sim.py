def euclidean_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError()
    if len(x)!= len(y):
        raise ValueError()
    index = 0
    sum_rest = 0
    for index in range(len(x)):
        e_dist = abs(x[index] - y[index]) ** 2
        sum_rest += e_dist
        index += 1
    rest = sum_rest**(1/2)
    return rest

def manhattan_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError()
    if len(x)!=len(y):
        raise ValueError()
    index = 0
    sum_rest = 0
    for index in range(len(x)):
        e_dist = abs(x[index] - y[index])
        sum_rest += e_dist
        index += 1
    return sum_rest

def jaccard_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError()
    intersection = set(x).intersection(set(y))
    union = set(x).union(set(y))
    return 1 - (len(intersection)/len(union))

def cosine_sim(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError()
    if len(x)!=len(y):
        raise ValueError()
    index = 0
    numerator = 0
    x_sum_e = 0
    y_sum_e = 0
    for feature in x:
        e_product = x[index]*y[index]
        numerator += e_product
        x_sum_e += x[index]**2
        y_sum_e += y[index]**2
        index += 1
    x_e_norm = x_sum_e**(1/2)
    y_e_norm = y_sum_e**(1/2)
    return numerator/(x_e*y_e_norm)
