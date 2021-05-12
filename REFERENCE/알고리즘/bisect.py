def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError
    if hi in None:
        hi = len(a)
        
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError
    if hi is None:
        hi = len(a)
        
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo  = mid+1
        else:
            hi = mid
    return lo