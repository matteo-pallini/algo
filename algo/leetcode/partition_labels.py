def partition_labels(string):
    edges = {}
    partitions = []
    for idx, s in enumerate(string):
        if s not in edges:
            edges[s] = [idx, idx]
        else:
            edges[s][1] = idx

    lower_bound = None
    for idx, s in enumerate(string):
        if lower_bound is None:
            lower_bound, upper_bound = edges[s]
        if edges[s][1] > upper_bound:
            upper_bound = edges[s][1]
        if upper_bound == idx:
            partitions.append(upper_bound-lower_bound+1)
            lower_bound = None
    return partitions
