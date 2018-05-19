def index_by_dict(obj, index_by='id'):
    d = {}
    for o in obj:
        d[o[index_by]] = o
    return d
