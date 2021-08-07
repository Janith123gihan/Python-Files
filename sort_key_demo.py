import functools as fntls
#sort_key_demo.py

def dist0(p):
    """
p - (x,y)

"""
    x,y = p[0],p[1]
    return (x**2 + y**2)**0.5

def dist32(p):
    x, y = p[0],p[1]

    dx = x - 3
    dy = y - 2
    return(dx * dx + dy * dy)**0.5

def dist_P(p,P):
    x, y = p[0],p[1]
    dx = x - P[0]
    dy = y - P[1]
    return (dx * dx + dy * dy)**0.5

dist34 = fntls.partial(dist_P, P = (3,4))
dist32nw = fntls.partial(dist_P, P = (3,2))

lst = ((1,5),(3,6),(4,2),(2,7),(7,3))

print(lst)
print(sorted(lst, key = dist0))

print(sorted(lst, key = dist32))

print(sorted(lst, key = dist34))

print(sorted(lst, key = dist32nw))
