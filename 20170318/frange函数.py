def frange(first,stop=0.0,step=1.0):
    if stop == 0.0:
        stop = first
        first = 0.0
    result = []
    while first < stop:
        result.append(float(first))
        first += step
    return result
        
        
